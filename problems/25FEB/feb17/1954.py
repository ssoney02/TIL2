T = int(input())
for tc in range(1, T+1):
    n = int(input())

    arr = [[0]*n for _ in range(n)]
    # print(arr)
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 방향 전환 용 델타 만들어둠
    num = 1
    i, j, k = 0, 0, 0
    while num <= n**2:
        # print(f'넣어야될 수: {num}')
        # print(f'i: {i}, j:{j}, k: {k}')
        arr[i][j] = str(num)
        num += 1
        oi = i
        oj = j
        i += delta[k][0]
        j += delta[k][1]
        # i,j를 갱신하고, 그 다음 k갱신한걸 그 다음 num에 대해 적용

        # 방향 전환 해야되는 경우:
        # 1. 인덱스가 arr 자체를 벗어난 경우,,
        # 2. 변한 i,j 위치에 0말고 다른 숫자가 있으면 방향전환...
        if (not (0 <= i < n and 0 <= j < n)) or arr[i][j] != 0 :
            # if arr[i][j] != 0:
            if k == 3:
                k = 0
            else:
                k += 1
            i = oi + delta[k][0]
            j = oj + delta[k][1]
        # print(f'다음 i:{i}, j:{j}, k:{k}')
    # print(arr)
    print(f'#{tc}')
    for a in arr:
        result = ' '.join(a)
        print(result)


