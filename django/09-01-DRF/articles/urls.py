from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.article_list),   # 이제부턴 url name도 필요 없음 -> 다 templates에서 썼던거라..
    path('articles/<int:article_pk>/', views.article_detail),
]
