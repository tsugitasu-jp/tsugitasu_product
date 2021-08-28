from rest_framework import status
from rest_framework.response import Response

from constants import ROLE_ALL, ROLE_TEACHER, ROLE_STUDENT


# ユーザは特定できているので、先生or生徒orALLを特定できれば良い
def role_permission(role: int):
    def deco(func):
        def wrapper(view, request, *args, **request_kwargs):
            if role == ROLE_TEACHER or role == ROLE_STUDENT:
                user_role = request.user.role
                if role != user_role:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            return func(view, request, *args, **request_kwargs)
        return wrapper
    return deco