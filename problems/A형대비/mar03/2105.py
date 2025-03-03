delta = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
# 부딪히면 방향 탐색하는게 아니라 매번 네방향 다 탐색해보고 진행하면서 init_i,init_j에 다시 도달하면
# 거리 max 값 출력 !
def find_route(depth, oi, oj, cnt):
    # 종료조건: 네 방향으로 다 이동했고(depth == 4 방향 틀때마다 depth+1넘김), init_i, init_j
    # 델타 시계방향으로 탐색
    # 이동할 수 있으면 이동( oi+delta[k] visited == 0
    # 아니면 델타 반시계 방향으로 탐색

    for k in range(4):
        new_i, new_j = oi + delta[k], oj+delta[k]
        if (0<=new_i<N) and (0<=new_j<N) and (cafe[new_i][new_j] not in check_dessert) and visited[new_i][new_j] == 0:
            cnt += 1
            visited[new_i][new_j] = 1       # 방문체
            check_dessert.append(cafe[oi][oj])
            find_route(depth+1, new_i, new_j)
            cnt -= 1
            visited[new_i][new_j] = 0
            check_dessert.pop()







T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    check_dessert = []
    for i in range(N):
        for j in range(N):
            if [i,j] not in [[0,0], [0, N-1], [N-1, 0], [N-1, N-1]]:
                find_route()