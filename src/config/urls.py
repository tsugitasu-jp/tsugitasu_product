"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from apiv1 import urls

from django.views import generic
from django import forms
from users.models import PhotoModel

class PhotoForm(forms.ModelForm):

    class Meta:
        model = PhotoModel
        fields = '__all__'


class Photo(generic.CreateView):
    model = PhotoModel
    form_class = PhotoForm
    template_name = 'upload.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(Photo, self).get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["photos"] = PhotoModel.objects.all()
        return context

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-v1/', include(urls)),
    path('', Photo.as_view()),
]





