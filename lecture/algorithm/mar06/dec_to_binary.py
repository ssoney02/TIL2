target = 74

def dec_to_binary(target):
    binary_number = ""

    while target > 0:
        remain = target % 2     # 2로 나눈 나머지
        binary_number = str(remain) + binary_number
        target = target //2     # 2로 나눈다.
    print(binary_number)

dec_to_binary(target)

