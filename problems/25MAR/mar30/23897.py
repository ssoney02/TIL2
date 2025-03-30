def binary_search(target, arr):
    global flag, cnt
    l = 0
    r = len(arr) - 1
    m = (l+r) // 2
    if l > r:
        return cnt
    if arr[m] == target:
        cnt += 1
        return cnt
    if arr[m] > target:
        # target이 중간값보다 작으면 왼쪽 구간 탐색
        if flag == -1 or flag == 1:
            # 처음 시작값이거나 직전에 오른쪽 구간을 다녀왔으면..
            # 아니면 그냥 return 하고
            flag = 0
            binary_search(target, arr[:m])
        else:
            return 0
    else:
        if flag == -1 or flag == 0:
            # 처음 시작 값이거나 직전에 왼쪽 구간을 다녀왔으
            flag = 1
            binary_search(target, arr[m+1:])

        else:
            return 0
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    # print(A)
    t_cnt = 0
    for b in B:
        flag = -1
        cnt = 0
        res = binary_search(b, A)
        t_cnt += res

    print(f'#{tc} {t_cnt}')
