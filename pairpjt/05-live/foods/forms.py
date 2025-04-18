from django import forms
from .models import Recipe, Ingredient


# 1
# class RecipeForm(forms.ModelForm):
#     # 식재료 정보 입력 필드
#     ingredients = forms.MultipleChoiceField(
#         choices=[
#             ('TMT', '토마토'),
#             ('OLV', '올리브'),
#             ('PAS', '파스타'),
#         ],
#         widget=forms.CheckboxSelectMultiple,
#         help_text='요리 재료를 선택하세요.',
#     )

#     class Meta:
#         model = Recipe
#         fields = '__all__'


# 2
class RecipeForm(forms.ModelForm):
    # 다대다 관계 설정 되어 있음 -> 재료 모델 조회해서 사용 가능
    # queryset으로 불러오면 multiplechoice 필드에 바로 들어감!
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Recipe
        fields = [
            'name',
            'description',
            'ingredients',
        ]
