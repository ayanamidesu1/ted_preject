from django.urls import path

from comment.views.get_comment import GetComment
from comment.views.get_reply_comment import GetReplyComment

urlpatterns = [
  path('GetComment/',GetComment.as_view(),name='GetComment'),
  #获取视频评论列表
  path('GetReplyComment/',GetReplyComment.as_view(),name='GetReplyComment'),
  #获取评论回复列表
]