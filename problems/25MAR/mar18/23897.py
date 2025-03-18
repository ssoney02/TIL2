def binary_search(l, r, target):
    global flag, g_flag
    if l > r:
        return -1
    if g_flag == -1:    # 조건에 안맞으니까 더 탐색할 필요가 없
        return -1

    m = (l + r) // 2
    # 검색하면 종료
    if arr[m] == target:
        return m

    # 왼쪽 확
    elif arr[m] > target:
        if flag == -1 or flag == 1:     # 처음 찾는거거나 직전에 오른쪽을 갔다왔으면
            flag = 0
            return binary_search(l, m-1, target)
        else:
            g_flag = -1
            return -1

    # 오른쪽 확인
    else:
        if flag == -1 or flag == 0:
            flag = 1
            return binary_search(m+1, r, target)
        else:
            g_flag = -1
            return -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    B = list(map(int, input().split()))
    arr.sort()

    cnt = 0

    for target in B:
        g_flag = 0
        flag = -1
        res = binary_search(0, N-1, target)
        if res != -1 and g_flag == 0:
            cnt += 1
    print(f'#{tc} {cnt}')
