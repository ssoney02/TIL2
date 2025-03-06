def binary_to_decimal(binary_str):
    # 1. binary_str 문자열 뒤에서부터 진행
    # 2. 각 자리에 맞는 수를 곱하면서, 겨로가에 더함
    decimal_number = 0
    pow = 0

    for digit in reversed(binary_str):
        if digit == '1':
            decimal_number += 2 ** pow

        pow += 1
    print(decimal_number)

binary_to_decimal('1001010')