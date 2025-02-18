data = [0,4,1,3,1,2,4,1]
n = len(data)

cnt = [0] * (max(data)+1) #max(data)가 idx 최대값이어야되니까.. 0부터 max(data)까지려면 길이는 +1
print(cnt)
for i in range(n):
    cnt[data[i]] += 1 # data각 요소에 해당하는 idx에 각 요소의 수 넣음
print(cnt)
for j in range(1, max(data)+1):
    cnt[j] += cnt[j-1]
print(cnt) # 누적합 리스트 만듦

temp = [0] * len(data)
print(temp)

for k in range(len(data)-1, -1, -1):
    idx = data[k]
    temp[cnt[idx] - 1] = data[k]
    cnt[idx] -= 1
    print(f'k:{k}')
    print(f'cnt: {cnt}')
print(temp)
