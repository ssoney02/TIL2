def bin_to_dec(num):
    dec_num = 0
    pow = 0
    for n in reversed(num):
        if n == '1':
            dec_num += 2 ** pow
        pow += 1
    print(dec_num)

bin_num = '10101001'

bin_to_dec(bin_num)


# 10 진수 -> 2진수
target = 74
def dec_to_bin(target):
    binary_number = ''

    while target > 0 :
        remain = target % 2
        binary_number += str(remain)
        target //= 2
    print(binary_number)

dec_to_bin(target)
