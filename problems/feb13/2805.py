T = int(input())

for tc in range(1, T+1):
    n = int(input())    # n은 항상 홀수

    farm = [list(map(int, input())) for _ in range(n)]
    # di, dj -> 농장 크기에 따라 달라짐
    # n-1 / 2 만큼,
    print(farm)
    k = (n-1) // 2
    cnt = 0
    d = []
    for m in range(-k, k + 1):
        # for r in range(-(k-m), k-m+1):
        if 0 <= abs(m) < n :
            r = k - abs(m)
            for l in range(-r, r+1):
                if 0 <= abs(l) < n:
                    # abs(m) + r = k가 되는 r값을 찾고
                    # -r부터 r까
                    d.append([m, l])
    print(d)
    i = n//2
    j = n//2
    print(f'i:{i}, j:{j}')
    for q in d:
        print(q)
        new_i = i + q[0]
        new_j = j + q[1]
        if 0 <= new_i < n and 0 <= new_j < n:
            cnt += farm[new_i][new_j]
        # cnt += val
        # print(type(val))
        # print(f'val:{farm[i + q[0]][j + q[1]]}')

    print(f'#{tc} {cnt}')