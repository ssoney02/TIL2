from django.contrib import admin
from django.urls import path
from . import views     # 같은 디렉토리에서 import(명시적 상대경로)

app_name = 'articles'
# dinner의 주소 -> articles/dinner/
# urlpatterns에 있는 주소들은 앞에 articles/까지가 반드시 붙어있는데 
# articles/articles/<int:num>/이라고 명시하는건 이상함..
urlpatterns = [
    path('', views.index),
    path('dinner/', views.dinner),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('<int:num>/', views.detail),
]
