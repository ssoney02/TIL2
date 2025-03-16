#트리에 값 채워넣기
def insert_val(p):
    global idx
    if p:           # p가 0이 아니면
        insert_val(left[p])
        tree[p] = nums[idx]
        idx += 1
        insert_val(right[p])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    nums = [i for i in range(1, N+1)]
    idx = 0
    # 트리 만들
    for i in range(1, N+1):
        if i * 2 < N:
            left[i] = 2 * i
            right[i] = 2 * i + 1
        if i * 2 == N:
            left[i] = 2 * i
    # 1부터 N까지 채워넣을
    insert_val(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')
