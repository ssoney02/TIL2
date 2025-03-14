import sys
sys.stdin = open('1861input.txt', 'r')
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
def find_room()
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i + delta[k][0], j + delta[k][1]
                if 0 <= ni < N and 0 <= nj < N and room[i][j] + 1 == room[ni][nj] and visited[ni][nj] == 0:
                    visited[i][j] = 1
                    break   # for k (어차피 숫자는 다 다르므로 이동가능한건 하나밖에 없음)
            else:           # 네 방향 다 돌았는데 더 이상 갈 곳이 없으면



