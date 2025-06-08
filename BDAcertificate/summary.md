## 작업형2 무작정 따라해보기
- X: 독립변수
- y: 종속변수

- .isnull().sum(): 결측치가 있는 금액 확인

- .fillna(0): 0을 결측치에 채움
- .head(): 기본값 5개. 특정 컬럼의 위에서 부터 5개 값만 보여줌. 개수 지정가능
- .tail(): 기본값 5개. 특정 컬럼의 아래에서부터 5개 값만 보여줌.


## tutorial T1 2회 기출유형
- .sort_values('f5', ascending=False) : f5컬럼 내림차순정렬

```py
# 'age' 컬럼 >= 80 인 데이터의 'f5' 컬럼 평균값 구하기
print(df[df['age']>=80]['f5'].mean())
```

- .iloc[행위치, 열위치]: 데이터프레임의 행위치, 열위치를 지정해서 작업수행   
-> 전체 데이터프레임의 구조를 보고 위치 확인해서 지정하는 형태
```py
# 데이터프레임의 0~9 행 의 -1열에 min값을 넣겠다.
df.iloc[:10,-1] = min
```

### 데이터 나누는 법
```py
# 데이터 셋의 앞에서 순서대로 70% 데이터만 활용해서...

# 1. 순서대로 데이터를 나누는 방법
data70, data30 = np.split(df, [int(.7*len(df))])

# 2. 랜덤으로 데이터를 나누는 방법 -> .sample 사용
data70 = df.sample(frac=0.7)  # 랜덤으로 70%의 데이터를 뽑음
data30 = df.drop(data70.index)  # 랜덤으로 뽑은 70%를 원래 df에서 drop -> 남은게 나머지 30

data70.tail()   # 아래에서 5개 데이터만 확인
```

### 표준편차 구하기
1. 모집단(데이터가 전체 일 때)
```py
np.std(data70['f1'])
```
2. 표본(데이터가 전체의 일부(샘플)일 때)
=> 대체로 얘를 쓰는게 맞을듯...
```py
data70['f1'].std()
```
<img src='./images/stdimg.png'>

---   
- 논리 연산자 사용 시 
각 조건에 대한 괄호 구분 명확히 해줘야됨!!!
```py
print(df[df['age'] > (med + 1.5*std) | df['age'] < (med - 1.5*std)]['age'].sum())  # TypeError 발생
print(df[(df['age'] > (med + 1.5*std)) | (df['age'] < (med - 1.5*std))]['age'].sum())  # ok

```

- .loc: 내부 조건을 사용해서 True/False로 필터링하고 True인 행만 가져옴
```py
# 이상치 상한 벗어나는 애들 필터링 + 이상치 하한 벗어나는 애들 필터링
df.loc[(df['age'] > max)]['age'].sum() + df.loc[(df['age'] < min)]['age'].sum()
```