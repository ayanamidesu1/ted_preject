from rest_framework.views import APIView
from django.db import connection
import json
from datetime import datetime
from ..log.log import Logger
from django.shortcuts import render
from django.http import JsonResponse

logger = Logger()
class GetComment(APIView):
    def request_path(self, request):
        request_path = request.path
        request_ip = request.META.get('REMOTE_ADDR', '未知IP')
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f'{request_ip} 在 {now} 访问了 {request_path}'

    def get(self, request):
        logger.warning(self.request_path(request) + str(request.user))
        return render(request, '404.html', status=404)

    def post(self,request,*args,**kwargs):
        try:
            data=json.loads(request.body.decode('utf-8'))
            video_id=data.get('video_id',None)
            limit=data.get('limit',10)
            offset=data.get('offset',0)
            if video_id:
                sql='''
                select *,comment_table.id as 'comment_id' ,video_info.id as 'video_id',auth_user.id as 'user_id',
                comment_interaction.id as 'in_id',comment_interaction.comment_id as 'in_comment_id'
                from comment_table left join video_info on video_info.id=comment_table.video_id 
                left join auth_user on auth_user.id=comment_table.send_user_id
                left join comment_interaction on comment_table.id=comment_interaction.comment_id and 
                comment_interaction.comment_type='comment'
                 where video_id=%s order by comment_table.send_time desc limit %s offset %s
                '''
                with connection.cursor() as cursor:
                    cursor.execute(sql,[video_id,limit,offset])
                    columns = [col[0] for col in cursor.description]
                    result = cursor.fetchall()
                    rows = [dict(zip(columns, row)) for row in result]
                    cursor.execute('select count(*) from comment_table where video_id=%s',[video_id])
                    total = cursor.fetchone()[0]
                    rows = {'rows':rows, 'total':total}
                    for row in rows['rows']:
                        del row['id']
                        del row['password']
                        del row['email']
                    return JsonResponse({'status':200, 'msg':'获取评论成功','data':rows},status=200)
            else:
                logger.warning(self.request_path(request)+f'参数错误:{data}')
                return JsonResponse({'status':400, 'msg':'参数错误'},status=400)

        except Exception as e:
            logger.error(str(e))
            return JsonResponse({'status':500, 'msg':'服务器错误'},status=500)
