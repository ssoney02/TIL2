import random
from django.shortcuts import render

# Create your views here.
# request를 반드시 view함수의 인자로 받아야됨!!! 약속!!
def index(request):
    # (메인 페이지가 담겨 있는) 응답 객체를 반환
    
    context = {
        'name': 'Jane',
    }
    
    # 페이지를 객체와 합쳐서 하나로 반환
    # render함수는 첫 번째 인자로 반드시 request를 받음!(약속)
    return render(request, 'articles/index.html', context)
    # render는 세개까지 인자 받을 수 o
    
def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육',]
    picked = random.choice(foods)
    # 일반적으로 딕셔너리 키-값 변수명 일치시킴.. 헷갈리니깐..
    context = {
        'foods' : foods,
        'picked': picked,
        
    }
    
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    print(request)  # <WSGIRequest: GET '/catch/?message=티니핑'>
    print(type(request))    # <class 'django.core.handlers.wsgi.WSGIRequest'>
    print(request.GET)  # <QueryDict: {'message': ['티니핑']}>
    print(request.GET.get('message'))   # 딕셔너리의 get()메소드 사용.. => 티니핑
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'articles/catch.html', context)

def detail(request, num):
    context = {
        'num' : num,
    }
    return render(request, 'articles/detail.html', context)