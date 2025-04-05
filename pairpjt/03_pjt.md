- 템플릿에서 조건에 따라 렌더링을 다르게 하고 싶은 경우

```python
# views.py
context = {
	'submitted': True,
}
return render(request, '', context)
```

```html
{% if submitted %}
{% endif %}
```

로 다르게 출력 가능


--- 

### <문제>

1. 같은 기업을 여러 번 검색 시, 중복된 내용들이 덮어씌어지지 않고 따로 계속 저장됨
    
    → filter(company_name=data)로 가져와서 context로 넘기기때문에 DB에 있는 같은 댓글들이 계속 추가돼서 출력됨..
    

2. model 정의 시, comments를 textfield로 설정(조건)
    - pk 하나에 기업 하나 , 댓글 여러 개 할당 됨
    - 댓글이 리스트 형식으로 들어가나, textfield이기 때문에 str 형태로 저장
    - .remove / 반복문 사용 시 에러
    - 해결 방안
        1. 모델 필드를 JSONfield로 변경
        2. json.loads() 사용
            
            → 파이썬 리스트 형식 (’)이 JSON(”)형식이 아니어서 파싱 불가..
            
        3. 댓글 하나를 하나의 레코드로 저장 (채택✔️)
    
    ➕ get_object_or_404(Model, 조건)
    
    : 해당 조건을 만족하는 객체가 있으면 가져오고, 없으면 404 페이지를 자동으로 반환