from collections import deque


def calculate(num):
    global M, visited

    q = deque([num])
    cnt_lst = [-1] * 1000001
    cnt_lst[num] = 0
    # print(q)

    while q:
        res = q.popleft()

        if res == M:
            return cnt_lst[res]
        # if cnt_lst[res] == -1:
        for n_res in [res+1, res-1, res*2, res-10]:
            if 0 <= n_res <= 1000000 and cnt_lst[n_res] == -1:
                q.append(n_res)
                cnt_lst[n_res] = cnt_lst[res] + 1
        # # if res + 1 < 1000000 and cnt_lst:
        #     q.append(res + 1)
        #
        # # if res - 1 > 0:
        #     q.append(res - 1)
        # # if res * 2 < 1000000:
        #     q.append(res * 2)
        # # if res - 10 > 0:
        #     q.append(res - 10)
        # # visited.append(res)
        # cnt_lst[res] = cnt_lst[num] + 1




T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cnt = 0
    visited = []
    ans = calculate(N)
    print(f'#{tc} {ans}')
