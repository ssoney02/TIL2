import heapq

delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 상, 우, 하, 좌


def dijkstra(i, j, K):

    pq = [(0, i, j, K)]  # 조작횟수, i좌표, j좌표
    control = [[float('inf')] * N for _ in range(N)]
    control[i][j] = 0
    # 이동만하면 control[i][j] = 1
    # 방향 전환 하고 이동하면 control[i][j] = 방향전환횟수 + 1
    # n_cnt = cnt + control[ni][nj]

    d = 0
    while pq:
        cnt, oi, oj, tmp_k = heapq.heappop(pq)
        if field[oi][oj] == 'Y':
            break
        if control[oi][oj] < cnt:
            continue


        ni, nj = oi + delta[d][0], oj + delta[d][1]

        if 0 <= ni < N and 0 <= nj < N:
            n_cnt = cnt + control[ni][nj]
            if field[ni][nj] == 'T' and tmp_k == 0:
                continue
            elif field[ni][nj] == 'T' and tmp_k > 0:
                tmp_k -= 1
        # 갈 수 없으면 회전해야됨 -> cnt += 1
        # 갈 수 있으면 그냥 계속 같은 방향으로 가면 됨
        else:
            # control[ni][nj] += ???
            pass

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    field = [input() for _ in range(N)]
