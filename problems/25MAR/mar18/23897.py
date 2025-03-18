def binary_search(l, r, target):
    if l > r:
        return -1
    m = (l+ r) // 2
    # 검색하면 종료
    if arr[m] == target:
        return m

    elif arr[m] > target:

    else:
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
