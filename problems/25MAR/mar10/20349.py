from collections import deque
def overhand(cards):
    shuffle_num = int(N * 0.37)
    shuffle_cards = cards[N-shuffle_num:]
    del cards[N-shuffle_num:]
    for i in range(len(shuffle_cards)-1, -1, -1):
        cards.insert(0, shuffle_cards[i])
    return cards

def perfect_shuffle(cards):
    shuffle_num = int(N * 0.5)
    shuffle_cards = deque()
    for c in cards[N-shuffle_num:]:
        shuffle_cards.append(c)
    del cards[N-shuffle_num:]
    cards = deque(cards)
    n_cards = []
    # N이 홀수이면 무조건 cards가 1개 더 많음
    for _ in range(N//2):
        n_cards.append(cards.popleft())
        n_cards.append(shuffle_cards.popleft())
    if cards:     # cards가 빈 리스트가 아니면
        n_cards.append(cards.popleft())
    return n_cards


TC = int(input())
for tc in range(1, TC+1):
    N, T = map(int, input().split())    # N: 카드 장 수, T: 셔플 set 시행 횟수
    # 셔플 set 1회: 오버핸드셔플 -> 퍼펙트 셔플
    card_lst = [i for i in range(1, N+1)]
    t = 1
    while t <= T:
        o_cards = overhand(card_lst)
        p_cards = perfect_shuffle(o_cards)
        card_lst = p_cards
        t += 1

    ans = []
    for c in card_lst:
        ans.append(str(c))
    res = ' '.join(ans)
    print(f'#{tc} {res}')


