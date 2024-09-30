from django.urls import path

from comment.views.add_comment import AddComment
from comment.views.get_comment import GetComment
from comment.views.get_reply_comment import GetReplyComment
from comment.views.interaction_comment import InteractionComment

urlpatterns = [
  path('GetComment/',GetComment.as_view(),name='GetComment'),
  #获取视频评论列表
  path('GetReplyComment/',GetReplyComment.as_view(),name='GetReplyComment'),
  #获取评论回复列表
  path('AddComment/',AddComment.as_view(),name='AddComment'),
  #添加评论
  path('InteractionComment/',InteractionComment.as_view(),name='InteractionComment'),
  #评论交互包括点赞和踩
]