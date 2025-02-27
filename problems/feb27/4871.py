def dfs(start):
    # if visited[start] == 0: # 아직 지난 적 없으면
    visited[start] = 1
    if start == G:
        return  # 그냥 함수 종료!
    for next in range(len(adj_lst[start])): # start=1 이면 next -> 4, 3
        if adj_lst[start][next] and not visited[adj_lst[start][next]]: # 이동할 수 있는 next노드가 존재하고, 방문한적 없으면! 이동
            dfs(adj_lst[start][next])


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_lst = [[] for _ in range(V+1)]
    # data = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    # for i in range(E):
    #     x,y = map(int, input().split())
    #     data[x][y] = 1
    result = 0
    for i in range(E):
        a, b = map(int, input().split())
        adj_lst[a].append(b)
        # adj_lst[b].append(a) 방향 있음 (양방향 고려 안해도 됨)
    # print(adj_lst)
    S, G = map(int, input().split())    # 출발점: S, 도착점: G -> 갈 수 있으면 1, 없으면 0 출력

    dfs(S)
    print(f'#{tc} {visited[G]}')