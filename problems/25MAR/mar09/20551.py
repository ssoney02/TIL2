def check_candy(smallnum, bignum):
    global res
    for i in range(smallnum):
        if 1 <= smallnum - i < bignum:
            smallnum -= i
            res += i
            return res, smallnum
    else:
        res = -1
        return res, smallnum
T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    res = 0
    res_i, n_B = check_candy(B, C)
    # print(res_i)
    if res != -1:
        res_j, n_A = check_candy(A, n_B)
    # print(res_j)
    # print(f'na: {n_A}')

    print(f'#{tc} {res}')

