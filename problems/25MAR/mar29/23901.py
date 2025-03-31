import heapq
delta = [[-1, 0], [0,1], [1,0], [0, -1]]
def dijkstra(si, sj):
    pq = [(0, si, sj)]
    fuels = [[float('inf')] * N for _ in range(N)]
    fuels[si][sj] = 0

    while pq:
        fuel, oi, oj = heapq.heappop(pq)
        if fuels[oi][oj] < fuel:        # 여기는 등호 붙이면 안됨! inf도 continue해버림..
            continue
        for d in delta:
            ni, nj = oi+d[0], oj+d[1]
            #
            if 0 <= ni < N and 0 <= nj < N:
                if graph[ni][nj] > graph[oi][oj]:
                    n_fuel = fuel + graph[ni][nj] - graph[oi][oj] + 1
                else:
                    n_fuel = fuel + 1
                if fuels[ni][nj] <= n_fuel:     # 여기는 등호 붙여줘야 동일한 경우 굳이 방문할 필요x
                    continue
                # 아니면
                fuels[ni][nj] = n_fuel  # 누적 fuel값 갱신!
                heapq.heappush(pq, (n_fuel, ni, nj))

    return fuels[-1][-1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # print(graph)
    res = dijkstra(0,0)

    print(f'#{tc} {res}')

