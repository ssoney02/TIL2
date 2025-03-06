# 10진수 -> 16진수
def decimal_to_hexadiecimal(target):
    hex_digit = "0123456789ABCDEF"
    hex_number = ""

    while target > 0:
        remain = target % 16
        hex_number = hex_digit[remain] + hex_number
        target //= 16

    print(hex_number)

decimal_to_hexadiecimal(256)