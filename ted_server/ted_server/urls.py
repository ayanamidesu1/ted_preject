from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.conf import settings
from django.conf.urls.static import static
from .get_csrf_token import CSRFTokenView
from .views import CustomTokenObtainPairView

urlpatterns = [
                  path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
                  #获取新token
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  #刷新token
                  path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
                  #验证token
                  path('api/user/', include('user.url'), name='user'),
                  #用户模块接口
                  path('api/csrf/', CSRFTokenView.as_view(), name='csrf'),
                  #获取csrf token
                  path('api/comment/', include('comment.url'), name='comment'),
                  #评论模块接口
                  path('api/video/', include('video.url'), name='video'),
                  #视频模块接口
              ] + static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')
