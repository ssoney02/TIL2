# import sys
# sys.stdin = open("23888input.txt", "r")

def bin_to_dec(binary_str):
    decimal_num = 0
    pow = 0

    for digit in reversed(binary_str):
        if digit == '1':
            decimal_num += 2 ** pow

        pow += 1
    result.append(str(decimal_num))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = [input().strip() for _ in range(N)]
    # print(num)
    result = []
    total_num = ''.join(num)
    for i in range(0, len(total_num), 7):
        # print(total_num[i:i+7])
        bin_to_dec(total_num[i:i+7])

    # print(total_num)
    # print(result)
    ans = ' '.join(result)
    print(f'#{tc} {ans}')