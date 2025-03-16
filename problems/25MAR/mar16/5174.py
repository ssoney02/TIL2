def pre_order(n):
    global cnt
    if n:
        pre_order(left[n])
        cnt += 1
        pre_order(right[n])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())    # 노드: 1~E+1
    trees = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    cnt = 0
    for i in range(E):
        p, c = trees[2*i], trees[2*i +1]
        if left[p] == 0:
            left[p] = c
        elif right[p] == 0:
            right[p] = c
    # print(left)
    # print(right)
    pre_order(N)
    print(f'#{tc} {cnt}')