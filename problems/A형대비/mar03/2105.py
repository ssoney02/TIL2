delta = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
# 부딪히면 방향 탐색하는게 아니라 매번 네방향 다 탐색해보고 진행하면서 init_i,init_j에 다시 도달하면
# 거리 max 값 출력 !

def find_route(k, oi, oj, cnt):
    global max_cnt


    # 한 방향씩 잡고 이동할 것
    # 한 방향으로 쭉 이동하다가 더 이상 갈 곳이 없으면 return 하고 나와서 다른 방향 탐색
    ni, nj = oi + delta[k], oj + delta[k]
    if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    check_dessert = []
    tmp_len = []
    max_cnt, max_result = -float('inf'), -float('inf')
    result = -1
    for i in range(N):
        for j in range(N):
            if [i, j] not in [[0,0], [0, N-1], [N-1, 0], [N-1, N-1]]:
                si, sj = i, j
                find_route(0, i, j, 0)
                # 시작점 별 max값이 max_cnt
                # 케이스 하나 당 max값은 max_result
                max_result = max(max_result, max_cnt)

    print(f'#{tc} {max_result}')