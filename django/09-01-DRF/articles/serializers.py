from rest_framework import serializers
from .models import Article


# 전체 게시글 목록을 직렬화하는 serializer 클래스
# 보통 다수의 데이터를 변환하는 serializer는 중간에 List를 넣음
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', )   # 클라이언트한테 어떤 데이터 구성을 줄 지 설계

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'