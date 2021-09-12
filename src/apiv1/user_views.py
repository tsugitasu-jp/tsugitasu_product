from datetime import datetime, timedelta

import pymongo
from pymongo.errors import DuplicateKeyError

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apiv1.authentication import FirebaseAuthentication
#from apiv1.decorator import role_permission
#from constants import ROLE_NONE, ROLE_ALL, ROLE_TEACHER, ROLE_STUDENT
from config.settings import tsugitasu_db

co_following = tsugitasu_db['users_following']
co_follower = tsugitasu_db['users_follower']
co_following.create_index( [("_f", pymongo.ASCENDING), ("_t", pymongo.ASCENDING)], unique=True )
co_follower.create_index( [("_f", pymongo.ASCENDING), ("_t", pymongo.ASCENDING)], unique=True )

# サインアップ: firebase側と同期して、mongoにuidを登録(drf-firebase-authのauthentication.pyのwrapperを呼ぶ)
class SignUpAPIView(APIView):
    authentication_classes = [FirebaseAuthentication, ]

    def get(self, request):
        return Response(status=status.HTTP_200_OK)


# ユーザ情報登録: Mongoに「表示名」「権限」「画像URL」を登録
class SetUserDataAPIView(APIView):
    authentication_classes = [FirebaseAuthentication, ]

    def post(self, request, *args, **kwargs):
        input_dict = request.data
        user = request.user
        user.displayname = input_dict['display_name']
        user.photo_url = input_dict['photo_url']
        user.save()

        return Response(status=status.HTTP_200_OK)


# ユーザフォロー: Following, Followerコレクションに関係を追加
class FollowCreateAPIView(APIView):
    authentication_classes = [FirebaseAuthentication, ]

    res = {
        "status": "OK",
        "mes": "フォローしました"
    }

    def get(self, request, uid):    
        user = request.user
        time = datetime.utcnow() + timedelta(hours=9),
        print(time)
        dic_following = {
            "created_at": time[0],
            "_f": user.uid, 
            "_t": uid
        }
        dic_follower={
            "created_at": time[0],
            "_f": uid,
            "_t": user.uid,
        }

        try:
            co_following.insert_one(dic_following)
        except DuplicateKeyError:
            pass

        try:
            co_follower.insert_one(dic_follower)
        except DuplicateKeyError:
            pass

        return Response(self.res)
        

# ユーザフォロー削除: Following, Followerコレクションから関係を削除
class FollowDeleteAPIView(APIView):
    authentication_classes = [FirebaseAuthentication, ]

    res = {
        "status": "OK",
        "mes": "フォローを削除しました"
    }

    def get(self, request, uid):
        user = request.user
        # followingコレクションから削除
        co_following.delete_one({'_f': user.uid, '_t': uid})

        # followerコレクションから削除
        co_follower.delete_one({'_f': uid,'_t': user.uid})

        return Response(self.res)


# フォロー数の取得
class FollowGetNumberAPIView(APIView):
    authentication_classes = []

    def get(self, request, uid):
        follow_objs = co_following.find(
            filter={'_f': uid},
        )
        follower_objs = co_follower.find(
            filter={'_f': uid},
        )
        return Response({
            "status": "OK",
            "follow": follow_objs.count(),
            "follower": follower_objs.count()
        })


# フォローしている人のリストを取得
class FollowListGetAPIView(APIView):
    authentication_classes = []

    def get(self, request, uid):
        cur = co_following.aggregate([
            {'$match': {'_f': uid}},
            {'$lookup': 
                {'from': "users_user", # 結合したいコレクション
                 'localField': "_t", # 結合するフィールド(入力側)
                 'foreignField': "uid", # 結合される側
                 'as': "inventory"}}, # 結果配列の出力フィールド名}
            {'$unwind': '$inventory'},
            {'$project': {'_t': True, 'inventory': True}}
        ])
        def fetch(x):
            dic = {}
            dic['uid'] = x['_t']
            dic['displayname'] = x['inventory']['displayname']
            dic['photo_url'] = x['inventory']['photo_url']
            return dic
        
        return Response({
            "follow_list": list(map(fetch, cur)),
        })


# フォローされている人のリストを取得
class FollowerListGetAPIView(APIView):
    authentication_classes = []

    def get(self, request, uid):
        cur = co_follower.aggregate([
            {'$match': {'_f': uid}},
            {'$lookup': 
                {'from': "users_user", # 結合したいコレクション
                 'localField': "_t", # 結合するフィールド(入力側)
                 'foreignField': "uid", # 結合される側
                 'as': "inventory"}}, # 結果配列の出力フィールド名}
            {'$unwind': '$inventory'},
            {'$project': {'_t': True, 'inventory': True}}
        ])
        def fetch(x):
            dic = {}
            dic['uid'] = x['_t']
            dic['displayname'] = x['inventory']['displayname']
            dic['photo_url'] = x['inventory']['photo_url']
            return dic
        
        return Response({
            "follower_list": list(map(fetch, cur)),
        })

