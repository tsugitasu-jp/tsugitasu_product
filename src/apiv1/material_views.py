import uuid
from datetime import datetime, timedelta

from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from apiv1.authentication import FirebaseAuthentication
from apiv1.decorator import role_permission
from config.settings import tsugitasu_db
from constants import ROLE_NONE, ROLE_ALL, ROLE_TEACHER, ROLE_STUDENT
from pymongo import ASCENDING
from bson.objectid import ObjectId


co_material = tsugitasu_db['material']
co_user = tsugitasu_db['users_user']

# 教材登録
class MaterialCreateAPIView(APIView):
    authentication_classes = [FirebaseAuthentication, ]

    @role_permission(ROLE_TEACHER)
    def post(self, request):
        user = request.user
        input_dic = request.data
        # 本当はここで検証
        input_dic['cid'] = str(uuid.uuid4()) # 派生版・更新版でも共通となるIDを振る
        input_dic['bid'] = 1 # ブランチを特定するID
        input_dic['mes'] = "オリジナル"
        input_dic['user_ref'] = user.uid
        input_dic['parent'] = input_dic['derived'] = None
        input_dic['is_original'] = True
        input_dic['comments'] = []
        input_dic['ver'] = 1
        input_dic['is_latest'] = True
        input_dic['good'] = input_dic['read'] = 0
        input_dic['created_at'] = datetime.utcnow() + timedelta(hours=9)

        co_material.insert_one(input_dic)

        return Response(status=status.HTTP_200_OK)


# 教材の木(history-tree)を取得
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

