import sys
sys.stdin = open("23888input.txt", "r")

def bin_to_dec(binary_str):
    decimal_num = 0
    pow = 0

    for digit in reversed(binary_str):
        if digit == '1':
            decimal_num += 2 ** pow

        pow += 1
    result.append(decimal_num)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = [input().strip() for _ in range(N)]
    print(num)
    result = []
    for n in num:
        bin_to_dec(n)

    print(result)