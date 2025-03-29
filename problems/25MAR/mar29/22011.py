import heapq
T = int(input())
def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [float('inf') for _ in range(N+1)]   # 누적거리 저장
    dists[0] = 0
    while pq:
        node, dist = heapq.heappop(pq)

        if dists[node] < dist:
            continue

        for nodes in graph[node]:
            next_node = nodes[0]
            next_weight = nodes[1]

            n_dist = dist + next_weight
            if dists[next_node] < n_dist:
                continue

            # 누적거리 값 갱신
            dists[next_node] = n_dist
            heapq.heappush(pq, (next_node, n_dist))
    return dists[N]


for tc in range(1, T+1):
    N, E = map(int, input().split())    # 정점 수: N+1, 간선 수: E
    graph = [[] for _ in range(N+1)]    # 인접 리스
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    res = dijkstra(0)
    print(f'#{tc} {res}')
