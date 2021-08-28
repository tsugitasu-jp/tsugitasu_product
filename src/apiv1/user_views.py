from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from apiv1.authentication import FirebaseAuthentication
from apiv1.decorator import role_permission
from constants import ROLE_NONE, ROLE_ALL, ROLE_TEACHER, ROLE_STUDENT


# サインアップ: firebase側と同期して、mongoにuidを登録(drf-firebase-authのauthentication.pyのwrapperを呼ぶ)
class SignUpAPIView(APIView):
    authentication_classes = [FirebaseAuthentication, ]

    def get(self, request):
        return Response(status=status.HTTP_200_OK)


# ユーザ情報登録: Mongoに「表示名」「権限」「画像URL」を登録
class SetUserDataAPIView(APIView):
    authentication_classes = [FirebaseAuthentication, ]

    @role_permission(ROLE_ALL)
    def post(self, request, *args, **kwargs):
        input_dict = request.data
        user = request.user
        print(user.displayname)

        user.displayname = input_dict['displayname']
        user.role = input_dict['role']
        user.photo_url = input_dict['photo_url']
        user.save()

        return Response(status=status.HTTP_200_OK)




