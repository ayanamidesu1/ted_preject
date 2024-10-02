from django.urls import path

from user.views.edit_user_info import EditUserInfo
from user.views.get_all_userinfo import GetAllUserInfo
from user.views.get_userinfo import GetUserInfo
from user.views.register import RegisterView

urlpatterns=[
    path('RegisterView/',RegisterView.as_view(),name='RegisterView'),
    #注册视图
    path('GetUserInfo/',GetUserInfo.as_view(),name='GetUserInfo'),
    #获取用户信息
    path('GetAllUserInfo/',GetAllUserInfo.as_view(),name='GetAllUserInfo'),
    #获取所有用户信息
    path('EditUserInfo/',EditUserInfo.as_view(),name='EditUserInfo'),
    #编辑用户信息
]