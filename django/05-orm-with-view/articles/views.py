from django.shortcuts import render, redirect
from .models import Article


# 메인 페이지를 응답하는 함수 (+ 전체 게시글 목록)
def index(request):
    # DB에 전체 게시글 요청 후 가져오기
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# 특정 단일 게시글의 상세 페이지를 응답(+ 단일 게시글 조회)
def detail(request, pk):
    # pk로 들어온 정수값을 활용해서 DB에 id가 pk인 게시글을 조회 요청
    article = Article.objects.get(pk=pk)  # 왼쪽 pk는 필드명, 오른쪽 pk는 입력으로 넣어준 변수명
    print(article)  # 단일 객체를 반환!
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

# 게시글을 작성하기 위한 form을 제공하는 함수
def new(request):
    return render(request, 'articles/new.html')

# 사용자로부터 데이터를 받아 저장하고 저장이 완료되었다는 페이지를 제공하는 함수
def create(request):
    # 사용자로부터 받은 데이터를 추출
    print(request.POST)
    title = request.POST.get('title')
    content = request.POST.get('content')
    # DB에 저장 요청(3가지 방법)
    # 1번 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()
    
    # 2번 방법 -> 사용!
    # save 전에 무언가를 .. 할 것임 앞으로.. (유효성 검사!)
    article = Article(title=title, content=content)
    article.save()
    # 3번 방법
    # Article.objects.create(title=title, content=content)
    # return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)  # 주소이름, variable routing이 있다면 입력
    # return redicrect('articles:index')    # 작성 후 메인페이지로 이동

def delete(request, pk):
    # 어떤 게시글을 지우는 지 먼저 조회
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    # 몇 번 게시글 정보를 보여줄 지 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 어떤 글을 수정하는지 먼저 조회
    article = Article.objects.get(pk=pk)
    # 사용자 입력 데이터를 기존 인스턴스 변수에 새로 갱신

    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk) 
