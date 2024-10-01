from django.urls import path

from video.views.get_video_info import GetVideoInfo
from video.views.recommend_video import RecommendVideo

urlpatterns=[
    path('GetVideoInfo/',GetVideoInfo.as_view(),name='GetVideoInfo'),
    #使用视频ID获取视频信息
    path('RecommendVideo/',RecommendVideo.as_view(),name='RecommendVideo'),
    #推荐视频

]