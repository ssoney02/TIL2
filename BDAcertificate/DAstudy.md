## 메모..
- kernel: IDE와 python 내 개발환경을 이어주는 역할
현재 코드가 어떤 환경에서 실행되고 있는지 지정해줘야됨


**read_csv()의 동작원리**
```py
outrange = df[df['age'] != np.trunc(df['age'])]
```
Q. 이런 식으로 조건을 걸었을 때 하나하나 순회하는 방식으로 비교 해서 넘기는건가? <br>
A. <br>
데이터 프레임을 한 행씩 순차적으로 처리하는건 x <br>
pandas: 내부적으로 벡터화 연산을 이용해 빠르게 처리(전체 데이터에 한 번에 적용) <br>
    -> 수천, 수만 개의 데이터가 있어도 for문 처럼 하나씩 순회하는 방식보다 훨씬 빠르고 효율적
- df['age'] : pandas.Series 객체 <br>
    - pandas의 boolean indexing으로, 조건에 맞는 행들만 필터링해서 outrange에 저장
