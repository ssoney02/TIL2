def post_order(n):
    global result
    if node[n] != 0 and left[n] != 0 and right[n] != 0:
        # if left[n] != '.' and right[n] != '.':
        post_order(left[n])
        # 부모 노드에 연산결과 넣어야됨
        post_order(right[n])

        if node[n] == '-':
            result = node[left[n]] - node[right[n]]
        elif node[n] == '+':
            result = node[left[n]] + node[right[n]]
        elif node[n] == '*':
            result = node[left[n]] * node[right[n]]
        elif node[n] == '/':
            if node[right[n]] == 0:
                return
            if node[left[n]] < 0:
                result = -(-node[left[n]] // node[right[n]])
            else:
                result = node[left[n]] // node[right[n]]
        node[n] = result
        # print(node[n])

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [list(input().split()) for _ in range(N)]
    node = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    # left[0], right[0] = 0,0
    for t in tree:
        lt = int(t[0])
        if len(t) > 2:
            node[lt] = t[1]
            left[lt] = int(t[2])
            right[lt] = int(t[3])
        else:
            node[lt] = int(t[1])
    result = 0
    #
    # print(node)
    # print(left)
    # print(right)

    post_order(1)


    print(f'#{tc} {node[1]}')