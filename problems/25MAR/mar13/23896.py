def check_triplet(player):
    global flag
    cnt_cards = [0] * 10
    for c in player:
        cnt_cards[c] += 1
        if max(cnt_cards) == 3:
            flag = 1

def check_run(player):
    global flag
    for c in player:
        if c + 1 in player and c + 2 in player:
            flag = 1



T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    N = len(cards)
    flag = 0
    res = 0
    player1, player2 = [], []
    for i in range(6):
        player1.append(cards[i * 2])
        check_triplet(player1)
        check_run(player1)
        if flag == 1:
            res = 1
            break # for i
        player2.append(cards[i * 2 + 1])
        check_triplet(player2)
        check_run(player2)
        if flag == 1:
            res = 2
            break


    print(f'#{tc} {res}')

