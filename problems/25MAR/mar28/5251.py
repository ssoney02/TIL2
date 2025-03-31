import heapq

def dijkstra(start):
    pq = [(0, start)]
    dists = [float('inf')] * (N+1)
    dists[start] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if dists[node] < dist:
            continue
        for next_info in graph[node]:
            next_dist = next_info[0]
            next_node = next_info[1]

            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:
                continue

            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))
    return dists[N]

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    start_node = 0
    graph = [[] for _ in range(N+1)]    # 인접 리스
    for _ in range(E):
        s, e, w = map(int, input().split())
