from itertools import combinations


T = int(input())
for tc in range(1, T+1):
    n, m, c = map(int, input().split()) # nxn: 전체 벌통, m: 인당 채취가능한 벌통 수, c: 최대 채취가능한 벌꿀 양
    honey = [list(map(int, input().split())) for _ in range(n)]

    # print(honey)
    # m칸 벌통 하나 고정시켜 놓고 그 안에서 for문 돌려서 for i in range(m[i]+1, n), for j in range(
    profit_lst = []
    for i in range(n):
        for j in range(n):
            profit1 = 0
            max_profit1 = 0

            # 작업자 1의 벌통
            # 전체 계속 순회
            if j + m <= n:
                b1 = honey[i][j:j+m]    # 작업자1의 벌통 고정
                # print(b1)
                max_sum = 0
                for k in range(m+1):
                    for num_set in combinations(b1, k):
                        total = sum(num_set)
                        if total <= c:
                            max_sum = max(max_sum, total)
                            profit1 = 0
                            for s in num_set:
                                profit1 += (s**2)
                            max_profit1 = max(max_profit1, profit1)
                # print(max_sum)
                # print(profit1)

            # 작업자 2는 작업자 1 다음 벌통들 부터 순회
            # 같은 줄에 남은 벌통이 있는 경우
            for i2 in range(i, n):

                # if i2 == i:
                #     for j2 in range(j+m, n):
                #         profit2 = 0
                #         max_profit2 = 0
                #         if j2+m <= n:
                #             b2 = honey[i2][j2:j2+m]
                #             max_sum = 0
                #             for k in range(m + 1):
                #                 for num_set in combinations(b2, k):
                #                     total = sum(num_set)
                #                     if total <= c:
                #                         max_sum = max(max_sum, total)
                #                         profit2 = 0
                #                         for s in num_set:
                #                             profit2 += (s ** 2)
                #                         max_profit2 = max(max_profit2, profit2)
                #             # print(max_sum)
                #             # print(profit1)
                #             profit_lst.append(max_profit1+max_profit2)
                # else:
                for j2 in range(n):
                    if i2 == i and j2 < j + m:
                        continue

                    profit2 = 0
                    max_profit2 = 0
                    if j2 + m <= n:
                        b2 = honey[i2][j2:j2+m]
                        max_sum = 0
                        for k in range(m + 1):
                            for num_set in combinations(b2, k):
                                total = sum(num_set)
                                if total <= c:
                                    max_sum = max(max_sum, total)
                                    profit2 = 0
                                    for s in num_set:
                                        profit2 += (s ** 2)
                                    max_profit2 = max(max_profit2, profit2)

                        # print(max_sum)
                        # print(profit1)
                        profit_lst.append(max_profit1 + max_profit2)
    print(f'#{tc} {max(profit_lst)}')
