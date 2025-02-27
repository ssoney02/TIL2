def dfs(a, N):  # a:출발점, N:마지막 정점
    visited = [0] * (N+1)
    stack = []
    result = []
    while True:
        if visited[a] == 0:     # 첫 방문이면
            visited[a] = 1      # 방문 흔적 남겨줌
            result.append(str(a))
        # for else!!
        for b in adj_lst[a]:    # adj_lst[a]: a 노드와 연결되어있는 모든 노드 정보 가짐
            if visited[b] == 0: # 연결되있는 노드가 아직 방문 안한 노드면 (가볼 수 있는 경로가 남아있음)
                stack.append(a) # a로 일단 이동
                # print(f'stack:{stack}')
                a = b           # b로 이동할 것임
                break
        else:                   # 더 이동할 수 있는 노드가 없음!! 이미 한번씩 다 방문해봤음 -> 다른 노드 봐야됨
            if stack:           # stack이 빈 리스트가 아니면..
                a = stack.pop() # 직전에 온 지점으로 돌아감 (위치 갱신)
                # print(f'bstack: {stack}')
            else:
                break

    ans = '-'.join(result)
    print(f'#1 {ans}')



v, e = map(int, input().split())
graph = list(map(int, input().split()))

adj_lst = [[] for _ in range(v+1)]
print(adj_lst)

for i in range(e):
    a, b = graph[i*2], graph[i*2+1]
    adj_lst[a].append(b)
    adj_lst[b].append(a)
    # 정점 탐색 시 숫자가 낮은 정점부터 방문 -> 오름차순 정렬..


dfs(1, v)

