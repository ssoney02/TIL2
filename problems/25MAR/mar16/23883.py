def insert_val(n, arr):
    global tree, i
    if n:       # n이 비어있지않으면 (0이 아니면!)
        insert_val(left[n], arr)
        tree[n] = arr[i]
        i += 1
        insert_val(right[n], arr)

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 1~N을 이진 탐색 트리에 저장!
    i = 0
    tree = [0]* (N+1)
    par = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    num_lst = [num for num in range(1, N+1)]
    for n in range(1, N):
        if n * 2 < N:
            left[n] = n * 2
            right[n] = n * 2 + 1
        elif n * 2 == N:
            left[n] = n * 2

    insert_val(1, num_lst)
    a = N//2
    print(f'#{tc} {tree[1]} {tree[a]}')
