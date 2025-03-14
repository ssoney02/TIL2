
from itertools import combinations


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()
    idx_lst = [i for i in range(N-1)]

    tmp_res = float('inf')
    flag = -1

    # for comb in combinations(idx_lst, 2):
    #     box1 = carrots[:comb[0]+1]
    #     box2 = carrots[comb[0]+1:comb[1]+1]
    #     box3 = carrots[comb[1]+1:]
    for a in range(N-2):
        for b in range(a+1, N-1):
            box1 = carrots[:a+1]
            box2 = carrots[a+1: b+1]
            box3 = carrots[b+1:]
            for i in box1:
                if i in box2 or i in box3:
                    break   # for i
                for j in box2:
                    if j in box3:
                        break   # for j
            else:
                if max(len(box1), len(box2), len(box3)) > N//2:
                    continue
                else:
                    flag = 0
                    tmp_diff = max(len(box1), len(box2), len(box3)) - min(len(box1), len(box2), len(box3))
                    tmp_res = min(tmp_res, tmp_diff)
    if flag == 0:
        res = tmp_res
    else:
        res = -1



    print(f'#{tc} {res}')
