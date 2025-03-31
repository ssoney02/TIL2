from django import forms
from .models import Article
# class ArticleForm(forms.Form):  # model이랑 이름 겹치면 안됨..!
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)     # forms에는 textfield가 없음...!

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'  # 던더스코어 -> 그냥 장고의 문법..!
        