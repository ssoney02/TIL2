from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer




# Create your views here.
# DRF로 view함수를 만들 때 필수 데코레이터!!! 안쓰면  500 에러 뜸!!!!!!!!
@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        # article의 모든 데이터를 조회해서 직렬화 해서 넘김
        articles = Article.objects.all()
        # 직렬화
        # 다수의 데이터면 many=True로 해줘야 다중데이터 변환 가능
        serializer = ArticleListSerializer(articles, many=True) 
        # DRF에서 제공하는 Response를 사용해 JSON 데이터를 응답
        # JSON 데이터는 serializer의 data 속성에 존재
        return Response(serializer.data)
    elif request.method == 'POST':
        # 원래는
        # form = ArticleForm(request.POST)
        # 사용자 입력 데이터를 클래스로 받아서 변환
        serializer = ArticleSerializer(data=request.data)    # 받아온 데이터를 아예 serializer로 넘김
        # 유효성 검사!!
        if serializer.is_valid():   # 장고 모델 폼의 is_valid랑은 다른거긴 한데.. 장고 측에서 똑같이 맞춰줌
            serializer.save()
            # 데이터 생성이 성공했을 경우 201 Created 응답
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #데이터 생성이 실패했을 경우 400 Bad request 응답
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        # 삭제 요청인 경우
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        # partial -> 부분수정!, False로 해두면 일부분만 수정해도 나머지 다 보내야 됨
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
