import heapq

def dijkstra(start_node):
    pq = [(0, start_node)]  # 누적 거리, 노드 번호
    dists = [INF] * V       # 누적 거리를 저장할 리스트
    dists[start_node] = 0   # 시작 노드 최단거리는 0

    while pq:
        dist, node = heapq.heappop(pq)

        # 이미 더 작은 경로로 온 적이 있다면 pass
        # 예제 그림: c로 가는 경로가 3 or 4
        if dists[node] < dist:
            continue
        for next_info in graph[node]:
            next_dist = next_info[0]    # 다음 노드로 가기 위한 가중치
            next_node = next_info[1]    # 다음 노드 번호

            # 다음 노드로 가기 위한 누적 거리
            new_dist = dist + next_dist

            if dist[next_node] <= new_dist:
                continue

            # next_node 까지 도착하는데 비용은 new_dist
            dist[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists

INF = int(21e8)  # 21억 (무한대를 의미한다고 가정)

V, E = map(int, input().split())  # 노드 수, 간선 수
start_node = 0  # 문제에 따라 다름
graph = [[] for _ in range(V)]  # 인접 리스트로 구현

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))  # 단방향 그래프!!

result_dists = dijkstra(0)
print(result_dists)