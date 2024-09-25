from django.urls import path

from user.views.register import RegisterView

urlpatterns=[
    path('RegisterView/',RegisterView.as_view(),name='RegisterView'),
    #注册视图
]