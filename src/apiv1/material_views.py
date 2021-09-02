import os
import shutil
import uuid
from datetime import datetime, timedelta

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from apiv1.authentication import FirebaseAuthentication
from apiv1.decorator import role_permission
from config.settings.base import MEDIA_ROOT, tsugitasu_db, env
from constants import ROLE_NONE, ROLE_ALL, ROLE_TEACHER, ROLE_STUDENT
from apiv1.material_func import contetn_upload_to_s3
from pymongo import ASCENDING
from bson.objectid import ObjectId

import numpy as np

co_material = tsugitasu_db['material']
co_user = tsugitasu_db['users_user']

# 教材登録
class MaterialCreateAPIView(APIView):
    authentication_classes = [FirebaseAuthentication, ]

    #@role_permission(ROLE_TEACHER)
    def post(self, request):
        #user = request.user
        input_dic = request.data
        # 本当はここで検証
        cid = input_dic['cid'] = str(uuid.uuid4()) # 派生版・更新版でも共通となるIDを振る
        bid = input_dic['bid'] = 1 # ブランチを特定するID
        input_dic['mes'] = "オリジナル"
        #input_dic['user_ref'] = user.uid
        input_dic['parent'] = input_dic['derived'] = None
        input_dic['is_original'] = True
        input_dic['comments'] = []
        vid = input_dic['ver'] = 1
        input_dic['is_latest'] = True
        input_dic['good'] = input_dic['read'] = 0
        input_dic['created_at'] = datetime.utcnow() + timedelta(hours=9)

        # file受信とローカルへ保存
        file = request.FILES['fd']
        file_path = f"{cid}/b{bid}/v{vid}/{file.name}"
        local_path = os.path.join(MEDIA_ROOT, file_path)
        default_storage.save(local_path, ContentFile(file.read()))
        
        # fileをs3に転送
        if env == "test":
            contetn_upload_to_s3(cid, bid, vid, file.name)
            local_media_cid_path = os.path.join(MEDIA_ROOT, f"{cid}")
            shutil.rmtree(local_media_cid_path)

        #co_material.insert_one(input_dic)

        return Response(status=status.HTTP_200_OK)


# 教材の木(history-tree)を取得 (機能番号22)
class HistoryTreeGetAPIView(APIView):
    authentication_classes = []
    keys = ["bid", "mes", "ver", "created_at", "display_name", "photo_url", "depth"]
    
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
            return {key: x[key] for key in self.keys}

        # bidの値毎に値を取得
        contents = []
        bid = 1
        while True:
            cursor = co_material.find(
                filter={'bid': bid}, 
                projection={'user_ref': 1, 'bid': 1, 'ver': 1, 'derived':1 , 'mes': 1, 'created_at': 1}, # cidは詳細ページで得られるので要らない
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
            #print(user)
            def join_user(x):
                x['display_name'] = user['displayname']
                x['photo_url'] = user['photo_url'] 
                return x
            dic_lst = list(map(join_user, cursor))
            dic_lst = list(map(to_depth, dic_lst))
            contents.append(dic_lst)
            bid += 1
        #print(contents)
        return Response(contents)


# 詳細表示用の教材データを取得 (機能番号21)
class GetMaterialAPIView(APIView):
    authentication_classes = []
    keys = ["mes", "uid", "display_name", "photo_url", "title", "context", "file_name", "content_image_main", "content_image_subs", "created_at", "tags", "comments", "good",]

    @role_permission(ROLE_NONE)
    def get(self, request, cid, bid, ver):
        user = request.user

        def to_dict(x):
            return {key: x[key] for key in self.keys}

        cursor = co_material.find(
            filter={'cid': cid, 'bid': bid, 'ver': ver},
            projection={"user_ref": 1 ,"mes": 1, "title": 1, "context": 1, "file_name": 1, "content_image_main": 1, "content_image_subs": 1, "created_at": 1, "tags": 1, "comments": 1, "good": 1}
        )


        # ユーザー情報を取得
        user_ref = cursor[0]['user_ref']
        user_cursor = co_user.find_one(
            filter={'uid': user_ref},
            projection={'displayname': 1, 'photo_url': 1}
        )

        def join_user(x):
            x['uid'] = user_ref
            x['display_name'] = user_cursor['displayname']
            x['photo_url'] = user_cursor['photo_url'] 
            return x

        dic_list = list(map(join_user, cursor))
        dic_list = list(map(to_dict, dic_list))

        return Response(dic_list[0])
