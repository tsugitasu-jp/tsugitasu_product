from django.urls import path

from apiv1.material_views import MaterialCreateAPIView, HistoryTreeGetAPIView
from apiv1.user_views import SignUpAPIView, SetUserDataAPIView


urlpatterns = [
    path('signup/', SignUpAPIView.as_view()),
    path('make_account/', SetUserDataAPIView.as_view()),
    path('content/create/', MaterialCreateAPIView.as_view()),
    path('get_content_tree/<str:cid>/', HistoryTreeGetAPIView.as_view()),
]
