N, M = map(int, input().split())


# 1. 그래프 저장하기
#   - 비어있는 그래프를 생성
#   - 그래프 정보를 입력받아 넣는다.
# 인접행렬 (N*N의 0 배열)
# graph = [[0] * N for _ in range(N + 1)]

def dfs(node):
    # 보통 그래프 문제들에서
    # ex) k개의 노드 방문했다면 종료
    # ex) N개 모두 방문했다면 경로 출력
    # if 종료 시 해야할 것들 or 가지치기:
    #   return


    print(node, end='')
    # visited[node] = 1  # 여기서 초기화 해줘도 됨(문제, 개발자마다 다름)

    # 내가 갈 수 있는 후보들을 모두 확인하면서, 한 군데로 진행
    # 현재 노드에서 인접한 노드들을 모두 확인하면서, 한 군데로 진행
    for next_node in graph[node]:
        # 이미 방문했다면 가지마라!
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)

# 인접 리스트(N*N([]))
graph = [[] for _ in range(N + 1)]

# for row in graph:
#     print(*row)

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)  # 양방향이라면, 뒤집어서 저장도 해줘야 됨

visited = [0] * (N + 1)  # 방문 여부 기록
visited[1] = 1  # 출발점 초기화
dfs(1)
