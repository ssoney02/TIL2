T = int(input())

for tc in range(1, T+1):
    n = int(input()) # 금액
    money_lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    num_lst = []
    for money in money_lst:
        num = n // money
        num_lst.append(str(num))
        n = n - money * num

    result = ' '.join(num_lst)
    print(f'#{tc}')
    print(f'{result}')