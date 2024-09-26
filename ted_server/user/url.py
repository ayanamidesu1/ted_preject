from django.urls import path

from user.views.get_userinfo import GetUserInfo
from user.views.register import RegisterView

urlpatterns=[
    path('RegisterView/',RegisterView.as_view(),name='RegisterView'),
    #注册视图
    path('GetUserInfo/',GetUserInfo.as_view(),name='GetUserInfo'),
    #获取用户信息
]