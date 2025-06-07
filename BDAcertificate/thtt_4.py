# 라이브러리
import pandas as pd

# 데이터 불러오기
X = pd.read_csv("data/X_train.csv")
y = pd.read_csv("data/y_train.csv")
test = pd.read_csv("data/X_test.csv")

# EDA
# isnull().sum() -> 결측치가 있는 금액 확인
print(X.isnull().sum())
print(test.isnull().sum())
print(X.info())

# 데이터 전처리
# 0이라는 값을 결측치에 채움
X = X.fillna(0)
test = test.fillna(0)

# train에서 id값은 필요 없으므로 삭제
X = X.drop(['cust_id'], axis=1)
# test의 id는 나중에 csv 파일 만들 때 필요
# pop해서 cust_id 변수 안에 잠시 넣어둠
cust_id = test.pop('cust_id')

# 피처 엔지니어링
# 범주형 변수 -> label encoding
from sklearn.preprocessing import LabelEncoder
# 주구매상품, 주구매지점 col을 encoding
cols = ['주구매상품', '주구매지점']
for col in cols:
  le = LabelEncoder()
  X[col] = le.fit_transform(X[col])
  test[col] = le.fit_transform(test[col])

# 모델링 & 하이퍼파라미터 튜닝 & 앙상블
from sklearn.ensemble import RandomForestClassifier
# 간단한 하이퍼파라미터 튜닝
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=2022)
model.fit(X, y['gender'])   # 학습
# print(model.score(X,y['gender']))
predictions = model.predict_proba(test)   #예측

# csv 파일 생성
output = pd.DataFrame({'cust_id': cust_id, 'gender': predictions[:,1]})
# print(output.head())
output.to_csv("0000.csv", index=False)