from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #获取新token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #刷新token
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #验证token
    path('api/user/',include('user.url'),name='user'),
    #用户模块接口
]
