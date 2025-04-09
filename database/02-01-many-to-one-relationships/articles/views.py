from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ArticleForm, CommentForm
from .models import Article, Comment


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 특정 게시글에 작성된 모든 댓글 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@login_required
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

def comments_create(request, article_pk):
    # 어떤 게시글에 작성되는 댓글인지 알려면 게시글 먼저 조회해야됨
    article = Article.objects.get(pk=article_pk)
    # Comment form을 활용한 댓글 생성
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        
        comment = comment_form.save(commit=False)
        # save 한 값이 결국 댓글이므로..
        # 외래키 데이터를 넣으려면 댓글 인스턴스가 필요한데
        # 댓글 인스턴스는 save()호출이 완료되어야 반환됨
        # commit 키워드를 False로 바꾸면
        # 댓글 인스턴스는 생성해주지만 실제 DB에 아직 저장 요청은 보내지 않음
        comment.article = article # 외래키에 외래 키 데이터 입력
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

def comments_delete(request, article_pk, comment_pk):
    # 어떤 댓글이 삭제되는 것인지 조회
    comment = Comment.objects.get(pk=comment_pk)
    # 방법 1 (방법2를 더 권장)
    # article_id = comment.article.pk 
    # return redirect('articles:detail', article_id)
    # 해서 삭제 전에 미리 저장해두는 방법도 가능
    comment.delete()
    return redirect('articles:detail', article_pk)
        