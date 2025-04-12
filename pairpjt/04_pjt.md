
### url
url 통일이 필요해보임
스켈레톤 코드에서 pjt04/로 다 scrapy에 지정해놨는데 accounts랑 contentfetch에 따로 url을 분리해서
통일감 부족
- 프로젝트 시작 시에 url 통일 시켜놓고 가는게 중요할 듯
~~같은 동작할 url을 각 app 파일에 만들어놔서 처음에 프로필 페이지 들어갈때 꼬였었음~~
### 인자 바로 함수로 넘기기
```html
<a href="{% url 'stock_finder' %}?stock_name={{ stock.stock_name|urlencode }}">
    {{ stock.stock_name }}
</a>
```
사용자가 profile.html에서 a태그를 클릭했을 때 stock_name을 그대로 stock_finder에 넘겨서
검색 인자로 줌
- GET 요청
```py
company_name = request.GET.get('stock_name', '').strip().lower()
```


<hr>

__스켈레톤 코드를 잘 보자..__
있는거 구현하느라 시간 다 씀..