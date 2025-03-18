arr = [i for i in range(1, 11)]
# visited = [] => 이번 문제에서는 사용할 필요가 x

# level: N개의 원소를 모두 고려하면
# branch: 집합에 해당 원소를 포함시키는 경우 or 안시키는 경우 2가지
# 누적 값
#   - 부분집합의 총합
#   - 부분집합에 포함된 원소들

def dfs(cnt, total, subset):
    if cnt == 10:
        return
    # 포함하는 경우
    dfs(cnt+1, total + arr[cnt], subset + [arr[cnt]])    # 리스트 + 리스트 가능..
    # 안하는 경우
    dfs(cnt+1, total, subset)