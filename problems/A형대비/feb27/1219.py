def dfs(start):


T = 10
for tc in range(1, T+1):
    tc_num, E = map(int, input().split())
    adj_lst = [[] for _ in range(100)]
    visited = [0] * 100
    graph = list(map(int, input().split()))
    for i in range(E):
        a, b = graph[i*2], graph[i*2+1]
        adj_lst[a].append(b)
    print(adj_lst)



