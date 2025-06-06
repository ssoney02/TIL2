def bin_to_dec(str_bin):    # 2진수 10진수 변환
    pow = 0
    dec_num = 0
    for b in reversed(str_bin):
        if b == '1':
            dec_num += 2**pow
        pow += 1
    return dec_num


def pre_order(n):
    global bin_num
    if n <= N:  # 노드 번호 범위 내에 있으면
        bin_num += trees[n]
        pre_order(2*n)
        pre_order(2*n+1)


def in_order(n):
    global bin_num
    if n <= N:  # 노드 번호 범위 내에 있으면
        in_order(2 * n)
        bin_num += trees[n]
        in_order(2*n+1)


def post_order(n):
    global bin_num
    if n <= N:  # 노드 번호 범위 내에 있으면
        post_order(2 * n)
        post_order(2*n+1)
        bin_num += trees[n]


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 정점 수
    nums = list(map(int,input().split()))
    trees = [-1] * (N+1)
    nodes = [-1] * (N+1)
    left, right = [-1]*(N+1), [-1]*(N+1)

    # 트리
    for i in range(1, N+1):
        trees[i] = str(nums[i-1])


    # 전위
    bin_num = ''
    pre_order(1)
    tmp_dec1 = bin_to_dec(bin_num)

    #중위
    bin_num = ''
    in_order(1)
    tmp_dec2 = bin_to_dec(bin_num)

    #후위
    bin_num = ''
    post_order(1)
    tmp_dec3 = bin_to_dec(bin_num)

    max_num = max(tmp_dec1, tmp_dec2, tmp_dec3)
    print(f'#{tc} {max_num}')
