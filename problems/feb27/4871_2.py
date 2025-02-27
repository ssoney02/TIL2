
def DFS(start):
    visited[start] = 1
    if start == G:
        return
    for next in range(1, V+1):
        if data[start][next] and not visited[next]:
            DFS(next)

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 인접 행렬
    data = [[0]*(V+1) for _ in range(V+1)]
    # 방문 표시용 리스트
    visited = [0] * (V+1)
    # 간선 정보 입력 받기
    for i in range(E):
        x, y = map(int, input().split())
        data[x][y] = 1
    # 시작지점 S, 도착지점 G
    S, G = map(int, input().split())
    result = DFS(S)
    print(f'#{tc} {result}')