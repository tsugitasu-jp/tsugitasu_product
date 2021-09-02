from django.urls import path

from apiv1.material_views import MaterialCreateAPIView, HistoryTreeGetAPIView, GetMaterialAPIView
from apiv1.user_views import SignUpAPIView, SetUserDataAPIView, FollowCreateAPIView, FollowDeleteAPIView 



urlpatterns = [
    path('signup/', SignUpAPIView.as_view()),
    path('make_account/', SetUserDataAPIView.as_view()),
    path('content/create/', MaterialCreateAPIView.as_view()),
    path('get_content_tree/<str:cid>/', HistoryTreeGetAPIView.as_view()),
    path('follow/create/<str:uid>', FollowCreateAPIView.as_view()),
    path('follow/delete/<str:uid>', FollowDeleteAPIView.as_view()),
    path('content/<str:cid>/b<int:bid>/v<int:ver>', GetMaterialAPIView.as_view()),
]
