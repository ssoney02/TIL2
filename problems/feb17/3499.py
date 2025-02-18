T = int(input())

for tc in range(1, T+1):
    n = int(input())

    cards = list(input().split())
    new_cards =[]
    # print(cards)
    #
    # print(g1)
    # print(g2)
    # n이 홀수인 경우
    if n % 2 != 0:
        g1 = cards[:n // 2 + 1]  # 홀수면 g1의 카드가 한 장 더 많음
        g2 = cards[n // 2 + 1:]
        for i in range(n//2): # g2 길이만큼(짧은것) 하나씩 꺼내서 둠둠
            new_cards.append(g1[i])
            new_cards.append(g2[i])

        new_cards.append(g1[-1])
    # n이 짝수인 경우
    else:
        g1 = cards[:n // 2]  # 홀수면 g1의 카드가 한 장 더 많음
        g2 = cards[n // 2 :]
        for i in range(n//2):
            new_cards.append(g1[i])
            new_cards.append(g2[i])

    # print(new_cards)
    result = ' '.join(new_cards)
    print(f'#{tc} {result}')