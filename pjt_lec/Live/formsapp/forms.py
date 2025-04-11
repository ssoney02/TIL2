from django import forms

from .models import Product


# form1 (일반 Form 예시)
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


# form2 (ModelForm 예시)
class ProductForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('ELEC', 'Electronics'),
        ('BOOK', 'Books'),
        ('FASH', 'Fashion'),
    ]
    category = forms.MultipleChoiceField(
        choices=CATEGORY_CHOICES,
        required=False,
        help_text='하나 이상의 카테고리를 선택하세요',
        widget=forms.CheckboxSelectMultiple,  # 체크박스 형태로 랜더링
    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'category']


# form3
class BaseForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()


# form4
class ExtendedForm(BaseForm):
    # name, email 은 상속받아 옴
    address = forms.CharField(max_length=100)


# form5
class WidgetForm(forms.Form):
    # widget -> 특정 필드에 묶이게 됨(필드 안에 작성)
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',    # 부트스트랩의 class
            },
        )
    )
    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'cols': 50,
                'style': 'resize: none;',
            }
        ),
        required=False,
    )
