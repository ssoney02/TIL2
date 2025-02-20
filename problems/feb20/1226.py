
import sys
sys.stdin = open("1226input.txt", "r")

from collections import deque
T = 10
def find_start (n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i, j
def bfs(i, j):
    visited = [[0]*100 for _ in range(100)]
    q = deque()  # 큐 생성
    q.append([i, j])     # 시작좌표 인큐
    visited[i][j] = 1

    while q:
        ti, tj = q.popleft()
        if maze[ti][tj] == 3:
            return 1

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj
            if 0 <= wi < 100 and 0 <= wj < 100 and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = 1
    return 0


for tc in range(1, T+1):
    case = int(input())
    maze = [list(map(int, input())) for _ in range(100)]

    si, sj = find_start(100)

    result = bfs(si, sj)
    print(f'#{tc} {result}')

