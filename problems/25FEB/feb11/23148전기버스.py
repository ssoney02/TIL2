T = int(input())

for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))
    arr = [0] * (n+1)
    for _ in charge:
        arr[_] = 1
    # print(arr)
    i = 0
    cnt = 0
    while True:
        if 1 not in arr[i+1:i+k+1]:
            print(f'#{tc} 0')
            break
        else:
            cnt += 1
            # i 갱신
            idx = []
            for j in range(1, k+1):
                if arr[i+j] == 1:
                    idx.append(i+j)
            # print(f'idx:{idx}')
            i = max(idx)
            # print(f'i: {i}')
        if i + k >= n:
            print(f'#{tc} {cnt}')
            break
