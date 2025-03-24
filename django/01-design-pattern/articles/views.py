from django.shortcuts import render

# Create your views here.
# request를 반드시 view함수의 인자로 받아야됨!!! 약속!!
def index(request):
    # (메인 페이지가 담겨 있는) 응답 객체를 반환
    
    # 페이지를 객체와 합쳐서 하나로 반환
    # render함수는 첫 번째 인자로 반드시 request를 받음!(약속)
    return render(request, 'articles/index.html')
    

