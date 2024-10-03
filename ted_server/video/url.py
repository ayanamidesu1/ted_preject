from django.urls import path

from .views.get_video_info import GetVideoInfo
from .views.recommend_video import RecommendVideo
from .views.video_interaction import VideoInteraction

urlpatterns=[
    path('GetVideoInfo/',GetVideoInfo.as_view(),name='GetVideoInfo'),
    #使用视频ID获取视频信息
    path('RecommendVideo/',RecommendVideo.as_view(),name='RecommendVideo'),
    #推荐视频
    path('VideoInteraction/',VideoInteraction.as_view(),name='VideoInteraction'),
    #视频互动
]