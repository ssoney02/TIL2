from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from django.db.models import Count
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 전체 게시글 데이터 조회
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        
        # articles는 django에서는 쓸 수 있는 queryset 데이터 타입이기 때문에
        # 우리가 만든 모델시리얼라이저로 변환 진행
        serializer = ArticleListSerializer(articles, many=True)
        
        # DRF에서 제공하는 Response를 사용해 JSON 데이터를 응답
        # JSON 데이터는 serializer의 data 속성에 존재
        return Response(serializer.data)

    # 게시글 생성 요청에 대한 응답
    elif request.method == 'POST':
        # 예전 코드
        # form = ArticleFrom(request.POST)
        # 사용자가 보낸 ㅈ데이터를 클래스로 받아서 직렬화
        serializer = ArticleSerializer(data=request.data)
        # 유효성 검사
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # 단일 게시글 데이터 조회
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    
    # 단일 게시글 데이터 조회 + 해당 게시글의 댓글 개수 계산해달라고 DB에 한번에 요청
    # article = Article.objects.annotate(num_of_comments=Count('comment')).get(pk=article_pk)
    article = get_object_or_404(
        Article.objects.annotate(num_of_comments=Count('comment')), 
        pk=article_pk,
        )
    
    print(article.pk)
    print(article.title)
    print(article.content)
    # 기존에 article 객체에는 없었지만, 결과에만 잠깐 포함된 데이터
    # 실제 article 데이터의 column이 변한 건 아님!
    print(article.num_of_comments)
    
    if request.method == 'GET':
        # ArticleSerializer 클래스로 직렬화를 진행
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        # 사용자가 보낸 수정 데이터를 직렬화
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        # serializer = ArticleSerializer(instance=article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# 댓글 전체 목록 조회
@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # 사용자가 보낸 새로운 댓글 데이터와 기존 댓글 데이터를 활용해 가공
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def comment_create(request, article_pk):
    # 어떤 게시글에 작성되는 댓글인 지 단일 게시글 조회
    article = Article.objects.get(pk=article_pk)
    # 사용자가 보낸 댓글 데이터를 가공
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # 외래키 -> 유효성 검사에서 걸림
        # 외래키는 외부로부터 들어오는 데이터가 아니라 우리가 찾아서 넣어야하는 값.. 
        # 유효성 검사에 들어가면 안됨 -> commentserializer에서 빼줘야
        serializer.save(article=article)    
        # 원래는..  comment = comment_form.save(commit=False)
        # comment.article = article
        # comment.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)