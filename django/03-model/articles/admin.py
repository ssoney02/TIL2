from django.contrib import admin
from .models import Article     # 명시적 상대 경로 / 동일 위치에 있는 models 모듈에서 article 클래스를 가져옴
# Register your models here.
admin.site.register(Article)