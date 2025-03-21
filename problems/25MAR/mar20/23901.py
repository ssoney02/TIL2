import heapq

delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def dijkstra(i, j):
    pq = [(0, i, j)]  # 누적 연료, i, j
    fuels = [[float('inf')] * N for _ in range(N)]
    fuels[i][j] = 0
    # 종료조건: 목적지 도달하면

    while pq:
        fuel, oi, oj = heapq.heappop(pq)


        if fuels[oi][oj] < fuel:  # 방문 체크
            continue

        for d in delta:
            ni, nj = oi + d[0], oj + d[1]

            if 0 <= ni < N and 0 <= nj < N:  # 이동 가능 조건
                if location[ni][nj] > location[oi][oj]:
                    next_fuel = fuel + (location[ni][nj] - location[oi][oj]) + 1
                else:
                    next_fuel = fuel + 1

                if fuels[ni][nj] <= next_fuel:
                    continue

                fuels[ni][nj] = next_fuel
                heapq.heappush(pq, (next_fuel, ni, nj))

    return fuels[-1][-1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 가로, 세로 칸 수
    location = [list(map(int, input().split())) for _ in range(N)]

    # print(location)

    ans = dijkstra(0, 0)
    print(f'#{tc} {ans}')