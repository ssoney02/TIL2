def in_order(node):

    if words[node]:    # 0이 아니면. 존재하는 정점이면
        in_order(left[node])
        result.append(words[node])
        in_order(right[node])
T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [list(input().split()) for _ in range(N)]
    # print(tree)
    words = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    # 트리 만들기기
    for t in tree:
        n = int(t[0])
        words[n] = t[1]
        lt = len(t)
        if lt >= 3:
            left[n] = int(t[2])
        if lt >= 4:
            right[n] = int(t[3])
    # print(words)
    # print(left)
    # print(right)

    result = []
    in_order(1)
    # print(result)
    ans = ''.join(result)
    print(f'#{tc} {ans}')