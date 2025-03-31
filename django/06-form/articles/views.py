from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# 메인 페이지를 응답하는 함수 (+ 전체 게시글 목록)
def index(request):
    # DB에 전체 게시글 요청 후 가져오기
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# 특정 단일 게시글의 상세 페이지를 응답 (+ 단일 게시글 조회)
def detail(request, pk):
    # pk로 들어온 정수 값을 활용 해 DB에 id(pk)가 pk인 게시글을 조회 요청 
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# # 게시글을 작성하기 위한 페이지를 제공하는 함수
# def new(request):
#     form = ArticleForm()    # form이라는 인스턴스 생성
#     # new는 데이터를 처음 작성하는 form이니까 받아올 인자가 없는게 당연!
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


# # 사용자로부터 데이터를 받아 저장하고 저장이 완료되었다는 페이지를 제공하는 함수
# def create(request):
#     # 이전 코드랑 비교해보새요..
    
#     # 사용자로부터 받은 데이터를 인자로 통째로 넣어서 form 인스턴스 생성
#     form = ArticleForm(request.POST)        # 통째로 집어넣고 인스턴스를 만듦..!(개수상관x)
#     # 데이터가 유효한 지 저장 전에 검사! (유효성 검사)
#     # 유효성 검사 통과하면 True, 아니면 False
#     if form.is_valid():
#         # 유효성 검사를 통과했다면 (데이터 저장)
#         article = form.save()   # save 메소드는 반환을 해줌
#         return redirect('articles:detail', article.pk)  # detail로 redirect하려는건데 detail은 article.pk가 필요함
#     # 유효성 검사를 통과하지 못했다면
#     # 현재 사용자가 게시글을 작성하는 템플릿(new 페이지)을 다시 한번 응답
#     context = {
#         # 왜 유효성 검사를 통과하지 못했는지에 대한 에러메세지 담고 있음 (처음에 사용자한테 입력받은 정보랑은 다름 추가정보를 포함함!)
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)
    
    
# new + create 함수 결합!
def create(request):
    # 1. 요청 메서드가 POST라면
    if request.method == 'POST':
        # 1.1. 사용자로부터 받은 데이터를 인자로 통째로 넣어서 form 인스턴스 생성
        form = ArticleForm(request.POST)
        # 1.2. 유효성 검사
        if form.is_valid():
            # 1.3. 유효성 검사 통과한다면 저장
            article = form.save()
            # 1.4. 상세 페이지로 리다이렉트
            return redirect('articles:detail', article.pk)
        # is_valid()를 통과하지 못했다면? context로 가야됨!
    # 2. 요청 메서드가 POST가 아니라면 (GET, PUT, DELETE ...)
    else:   # new
        # 2.1. Articleform 인스턴스를 생성
        form = ArticleForm()
    # case 1 : 1.2에서 내려왔을 때 : 에러메시지를 담은 form
    # case 2 : 2.1이 끝나고 내려왔을 때 : 빈 form
    context = {
        'form' : form, 
    }
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    # 어떤 게시글을 지우는지 먼저 조회
    article = Article.objects.get(pk=pk)
    # DB에 삭제 요청
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     # 몇번 게시글 정보를 보여줄지 조회
#     article = Article.objects.get(pk=pk)
#     # 기존 정보 기반 수정할 수 있게 해야됨 -> ArticleForm의 인자로 채워넣을 것!
#     form = ArticleForm(instance=article)    # 그냥 ModelForm의 키워드 인자가 이런 형식으로 되어있음..
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)


# def update(request, pk):
#     # 어떤 글을 수정하는지 먼저 조회
#     article = Article.objects.get(pk=pk)
    
#     # 사용자가 새로 입력한 데이터를 받아서 form 인스턴스 생성
#     # save메서드는 instance 키워드 인자를 통해서 저장인지 수정인지를 판단함! 
#     # 없으면 create로직이랑 동일한 구조라 update가 아니라 create를 하게 됨!!!
#     form = ArticleForm(request.POST, instance=article)
    
#     if form.is_valid():
#         form.save()     # 저장할 건지 수정할 건지를 판단해야됨!
#         return redirect('articles:detail', article.pk)
#     context = {
#         'article' : article, 
#         'form': form,
#     }    
#     return render(request, 'articles/edit.html', context)
    
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
    