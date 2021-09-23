# from _typeshed import NoneType
import os
import shutil
import uuid
from datetime import date, datetime, timedelta


from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from apiv1.authentication import FirebaseAuthentication
from apiv1.decorator import role_permission
from config.settings import MEDIA_ROOT, tsugitasu_db, env
from constants import ROLE_NONE, ROLE_ALL, ROLE_TEACHER, ROLE_STUDENT
from apiv1.material_func import FileManager
from pymongo import ASCENDING, DESCENDING
from bson.objectid import ObjectId

import numpy as np

co_material = tsugitasu_db['material']
co_user = tsugitasu_db['users_user']

# 教材登録


class MaterialCreateAPIView(APIView):
    authentication_classes = [FirebaseAuthentication, ]

    @role_permission(ROLE_TEACHER)
    def post(self, request):
        user = request.user
        input_dic = {}

        # 本当はここで検証
        cid = input_dic['cid'] = str(uuid.uuid4())  # 派生版・更新版でも共通となるIDを振る
        bid = input_dic['bid'] = 1  # ブランチを特定するID
        vid = input_dic['ver'] = 1

        input_dic['title'] = request.data['title']
        input_dic['context'] = request.data['context']
        input_dic['tags'] = request.data.getlist('tag[]')
        input_dic['tag_flag'] = request.data['tag_flag']

        input_dic['mes'] = "オリジナル"
        input_dic['user_ref'] = user.uid
        input_dic['parent'] = input_dic['derived'] = None
        input_dic['is_original'] = True
        input_dic['comments'] = []
       
        input_dic['is_latest'] = True
        input_dic['good'] = input_dic['read'] = 0
        input_dic['created_at'] = datetime.utcnow() + timedelta(hours=9)

        # file受信とローカルへ保存
        file = request.FILES['fd']
        image_main = request.FILES['image_main']
        image_subs = request.FILES.getlist('image_sub[]')

        # file_managerの作成
        f_manager = FileManager(file, image_main, image_subs, cid, bid, vid)

        # testの場合はaws-sdk初期化
        if env == "test":
            f_manager.test_init()

        # fileの保存
        input_dic['file_name'] = f_manager.file_save_to_media()

        # 見出し画像の保存
        input_dic['content_image_main'] = f_manager.main_img_save_to_media()

        # 副画像の保存
        input_dic['content_image_subs'] = f_manager.sub_imgs_save_to_media()

        # fileをs3に転送
        if env == "test":
            f_manager.contetns_upload_to_s3(
                [input_dic['file_name'], 
                input_dic['content_image_main'], 
                *input_dic['content_image_subs']]
            )

        # localに作成したファイルを削除
        if env == "test":
            local_media_cid_path = os.path.join(MEDIA_ROOT, f"{cid}")
            shutil.rmtree(local_media_cid_path)

        co_material.insert_one(input_dic)

        return Response(status=status.HTTP_200_OK)


# 教材の木(history-tree)を取得 (機能番号22)
class HistoryTreeGetAPIView(APIView):
    authentication_classes = []
    keys = ["_id", "cid", "bid", "vid", "mes", "ver", "created_at", "author", "parent",
        "photo_url", "depth", "is_latest", "derived", "left", "right", "top", "bottom"]
    
    @role_permission(ROLE_NONE)
    def get(self, request, cid):
        # verとブランチidからノードの深さを算出
        def to_depth(x):
            # 派生元情報の取得
            d_ver = 0
            if x['derived'] is not None:
                d_ver = co_material.find_one(
                    filter={'_id': ObjectId(x['derived'])},
                    projection={'ver': 1}
                )['ver']
            # 派生元のver値+ノードのver値
            x['depth'] = x['ver'] + d_ver
            x['vid'] = x['ver']
            return {key: x[key] for key in self.keys}

        # bidの値毎に値を取得
        contents = []
        bid = 1
        while True:
            cursor = co_material.find(
                filter={'bid': bid}, 
                projection={'user_ref': 1, 'cid': 1, 'bid': 1, 'ver': 1, 'derived':1 , 'mes': 1, 'created_at': 1, 'is_latest': 1, 'parent': 1}, # cidは詳細ページで得られるので要らない
                sort=[('created_at', ASCENDING)]
            )
            if cursor.count() == 0:
                break

            # ユーザ情報を取得
            user_ref = cursor[0]['user_ref']
            user = co_user.find_one(
                filter={'uid': user_ref},
                projection={'displayname': 1, 'photo_url': 1}
            )
            # print(user)
            
            def join_user(x):
                x['author'] = user['displayname']
                x['photo_url'] = user['photo_url']
                return x
            def consider_node(x):
                x['left'] = True
                x['right'] = True
                x['top'] = False
                x['bottom'] = False
                x['_id'] = str(x['_id'])
                #if x['is_latest']:
                #    x['right'] = False
                return x
                
            def format_date(x):
                td = datetime.now() - x['created_at']
                day = td.days
                if day < 0:
                    x['created_at'] = "error"
                elif day == 0:
                    x['created_at'] = "今日"
                elif day == 1:
                    x['created_at'] = "昨日"
                elif day <= 30:
                    x['created_at'] = f"{day}日前"
                elif day <= 359:
                    x['created_at'] = f"{day % 30}ヵ月前"
                else:
                    x['created_at'] = x['created_at'].date()
                return x

            dic_lst = list(map(join_user, cursor))
            dic_lst = list(map(consider_node, dic_lst))
            dic_lst = list(map(to_depth, dic_lst))
            dic_lst = list(map(format_date, dic_lst))
            
            contents.append(dic_lst)
            bid += 1
        #print(contents)

        for i, content in enumerate(contents):
            if i == 0:
                continue
            # depth分の配列要素を調整で差し込む
            for j in range(content[0]['depth'] - 1):
                contents[i].insert(0, 
                    {
                        "top": False,
                        "right": False,
                        "bottom": False,
                        "left": False,
                        "mes":"",
                        "author":"",
                        "created_at":"",
                        "derived": "",
                        "parent": "",
                    },
                )
                
            for k, elem in enumerate(content):
               if (elem['derived'] is not None) and (elem['parent'] is None):
                    # depth探索
                    target_lst = contents[0]
                    target_num = -1
                    for j, dic in enumerate(target_lst):
                        if dic['_id'] == elem['derived']:
                            target_num = j
                            break
                    contents[0][target_num]['bottom'] = True
                    contents[i][k-1]['right'] = True

                    # top/bottom設定(対象のbidより低いbidの同一depthに関し、top/bottom設定)
                    for j in range(i, 0, -1):
                        contents[j][k-1]['top'] = contents[j][k-1]['bottom'] = True
                    break
       
        return Response({
            "contents": contents,
        })

# 詳細表示用の教材データを取得 (機能番号21)
class GetMaterialAPIView(APIView):
    authentication_classes = []
    keys = ["mes", "uid", "displayname", "photo_url", "title", "is_latest", "cid", "bid",
        "context", "file_name", "content_image_main", "content_image_subs", "created_at", "tags", "comments", "good",]

    def get(self, request, cid, bid, ver):
        def to_dict(x):
            return {key: x[key] for key in self.keys}

        cursor = co_material.find(
            filter={'cid': cid, 'bid': bid, 'ver': ver},
            projection={"user_ref": 1, "mes": 1, "title": 1, "context": 1, "file_name": 1, "content_image_main": 1,
                        "content_image_subs": 1, "created_at": 1, "tags": 1, "comments": 1, "good": 1, "is_latest": 1,
                        "cid": 1, "bid": 1}
        )

        if cursor.count() == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # ユーザー情報を取得
        user_ref = cursor[0]['user_ref']
        user_cursor = co_user.find_one(
            filter={'uid': user_ref},
            projection={'displayname': 1, 'photo_url': 1}
        )

        def join_user(x):
            x['uid'] = user_ref
            x['displayname'] = user_cursor['displayname']
            x['photo_url'] = user_cursor['photo_url'] 
            return x

        dic_list = list(map(join_user, cursor))
        dic_list = list(map(to_dict, dic_list))

        # 最新版じゃなければ最新版のver値を返す
        # print(dic_list)
        if not dic_list[0]['is_latest']:
            dic_list[0]['latest_vid'] = co_material.find_one(
                filter={'cid': cid,'bid': bid, 'is_latest': True},
                projection={'ver': 1}
            )['ver']

        return Response(dic_list[0])


# 最近投稿した教材の取得 (機能番号42)
class GetLatestMaterialsAPIView(APIView):
    authentication_classes = [FirebaseAuthentication, ]
    keys = ["cid", "bid", "context", "ver", "title", "content_image_main",
            "tags", "created_at", "display_name", "photo_url"]

    def get(self, request):
        user = request.user
        if user.uid is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        def to_dict(x):
            return {key: x[key] for key in self.keys}

        cursor = co_material.find(
            filter={'user_ref': user.uid, 'is_latest': True},
            projection={"title": 1, "context": 1, "content_image_main": 1,
                        "created_at": 1, "tags": 1, "cid": 1, "bid": 1, "ver": 1},
            limit=6,
            sort=[('created_at', DESCENDING)]
        )

        user_cursor = co_user.find_one(
            filter={'uid': user.uid},
            projection={'displayname': 1, 'photo_url': 1},
        )

        def join_user(x):
            x['display_name'] = user_cursor['displayname']
            x['photo_url'] = user_cursor['photo_url']
            return x
        
        def format_date(x):
            td = datetime.now() - x['created_at']
            day = td.days
            if day < 0:
                x['created_at'] = "error"
            elif day == 0:
                x['created_at'] = "今日"
            elif day == 1:
                x['created_at'] = "昨日"
            elif day <= 30:
                x['created_at'] = f"{day}日前"
            elif day <= 359:
                x['created_at'] = f"{day % 30}ヵ月前"
            else:
                x['created_at'] = x['created_at'].date()
            return x

        dic_list = list(map(join_user, cursor))
        dic_list = list(map(to_dict, dic_list))
        dic_list = list(map(format_date, dic_list))

        return Response(dic_list)


# いいね数のカウント(機能番号26)
class AddGoodAPIView(APIView):
    authentication_classes = [FirebaseAuthentication,]
    # keys = ["cid", "bid", "context", "ver", "title", "content_image_main", "tags", "created_at", "display_name", "photo_url"]

    def get(self, request, cid, bid, ver):
        user = request.user
        # uid非保持の場合はいいねを押せないようにする
        if user.uid is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        # 教材の情報を取得
        cursor = co_material.find(filter={'cid': cid, 'bid': bid, 'ver': ver, 'good_contents': {'$in': [user.uid]}})

        if cursor.count() == 0:
            result = co_material.update_one({'cid': cid, 'bid': bid, 'ver': ver}, {'$inc': {'good': 1}, '$push': {'good_contents': user.uid}})
        elif cursor.count() == 1:
            result = co_material.update_one({'cid': cid, 'bid': bid, 'ver': ver}, {'$inc': {'good': -1}, '$pull': {'good_contents': user.uid}})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)


# 指定した条件に沿って教材を取得
class GetMaterialsAPIView(APIView):
    authentication_classes = []
    keys = ["cid", "bid", "ver", "title", "context", "created_at", "content_image_main", "display_name"]
    
    def get(self, request):
        if "op" in request.GET:
            # query_paramが指定されている場合の処理
            op = request.GET.get("op")
            if op == "evaluation":
                result = co_material.find(
                    filter={'is_latest': True, 'bid': 1},
                    sort=[('good',DESCENDING),('created_at',DESCENDING)],
                    projection={'user_ref': 1, 'cid': 1, 'bid': 1, 'ver': 1, 'title': 1, 'context': 1, 'display_user': 1, 'content_image_main': 1, 'created_at': 1}
                )
            if op == "create":
                result = co_material.find(
                    filter={'is_latest': True, 'bid': 1},
                    sort=[('created_at', DESCENDING)],
                    projection={'user_ref': 1, 'cid': 1, 'bid': 1, 'ver': 1, 'title': 1, 'context': 1, 'display_user': 1, 'content_image_main': 1, 'created_at': 1}
                )
        
        def join_user(x):
            user_cursor = co_user.find_one(
                filter={'uid': x['user_ref']},
                projection={'displayname': 1, 'photo_url': 1},
            )
            x['display_name'] = user_cursor['displayname']
            x['photo_url'] = user_cursor['photo_url']
            return x
        
        def to_dict(x):
            return {key: x[key] for key in self.keys}

        def format_date(x):
            td = datetime.now() - x['created_at']
            day = td.days
            if day < 0:
                x['created_at'] = "error"
            elif day == 0:
                x['created_at'] = "今日"
            elif day == 1:
                x['created_at'] = "昨日"
            elif day <= 30:
                x['created_at'] = f"{day}日前"
            elif day <= 359:
                x['created_at'] = f"{day % 30}ヵ月前"
            else:
                x['created_at'] = x['created_at'].date()
            return x

        dic_list = list(map(join_user, result))
        dic_list = list(map(to_dict, dic_list))
        dic_list = list(map(format_date, dic_list))
        
        return Response(dic_list)