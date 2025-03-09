from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]
    # print(lines)
    # (1,2), (1,3), (2,3) : 조합! NC2
    # 조합 구하고 크기비교 해서 A랑 B랑 부등호 방향이 다르면 교차점 수 += 1
    cnt = 0
    for comb in combinations(lines, 2):
        # print(comb)
        if (comb[0][0] > comb[1][0] and comb[0][1] < comb[1][1]) or (comb[0][0] < comb[1][0] and comb[0][1] > comb[1][1]):
            cnt += 1
    print(f'#{tc} {cnt}')