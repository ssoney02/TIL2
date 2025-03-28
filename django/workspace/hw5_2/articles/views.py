from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    # 게시글 생성을 위한 form 제공
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    articles = Article(title=title, content=content)
    articles.save()
    
    return redirect('articles:index')   # redirect는 request를 인자로 받지 않음!!!