import sys
sys.stdin = open("1959input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_sum = 0
    if len(a) > len(b):
        a, b = b, a

    # total += a[i]*b[j]
    # j in range(i, i+len(a)-1)
    # i 범위 따로 돌리고
    # j범위 따로 돌리기..?
    for k in range(len(b)-len(a)+1):
        total = 0
        # j = k + i
        for i in range(len(a)):
            j = k + i

            # print(f'a:{a[i]}, b:{b[j]}')
            total += a[i] * b[j]
            # print(f'total: {total}')
        max_sum = max(max_sum, total)
    print(f'#{tc} {max_sum}')


