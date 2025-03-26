from django.db import models

# Create your models here.

# 게시글이 저장될 테이블을 설계하는 클래스

class Article(models.Model):
    # 제목 길이를 10글자로 제한한 것
    title = models.CharField(max_length=10) # 타이틀은 어떻게 보면 인스턴스!
    content = models.TextField()
    # 추가 필드
    # 글을 작성한 날짜, 시간은 보통 사용자가 직접입력하지 않음!
    # 자동으로 넣는 동작 추가
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)