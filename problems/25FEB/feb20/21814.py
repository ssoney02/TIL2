
def bfs(i, j, n):
    visited = [[0] * n for _ in range(n)]
    q = []
    q.append([i, j])     # 시작점 인큐
    visited[i][j] = 1 # 시작점 인큐 표시

    while q:    # q가 빈리스트가 아닐 동안 (q에 남은 칸이 없을 때까지)
        ti, tj = q.pop(0)   # ti, tj는 직전 좌표(popleft했으니까..)
        if maze[ti][tj] == 3:   # 종점에 도착하면!
            return visited[ti][tj] - 2

        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]: # 4방향 확인하면서 갈 수 있는 곳 인큐
            wi, wj = ti+di, tj+dj
            if 0 <= wi < n and 0 <= wj < n and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi,wj])   # 인큐
                visited[wi][wj] = visited[ti][tj] + 1 # 앞에꺼보다 하나씩 늘림 => 얼마나 왔는지 거리 확인 가능(칸수)


    return 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]

    # print(maze)
    # 0: 통로, 1: 벽, 2: 출발, 3: 도착

    # 시작점 찾아야됨
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                sti, stj = i, j

    ans = bfs(sti, stj, n)
    print(f'#{tc} {ans}')


