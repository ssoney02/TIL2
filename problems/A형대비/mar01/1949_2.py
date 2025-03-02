import sys
sys.stdin = open("1949input.txt", "r")
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def find_route(oi, oj, left_k):
    # oi,oj: 현재 위치
    # left_k: 남은 k
    global cnt, max_cnt
    original_k = left_k
    # 종료 조건: 네 방향 탐색 다 했고, left_k까지 적용해봤는데, 더 갈 곳이 없으면 return
    # 깎을 필요 없이 계속 이동가능해도 마지막에 1까지 왔을때 주변을 깎아서 1보다 작아지면 더 진행가능!
    # 최종 종료는 left_k == 0 인 상황
    if left_k == 0:
        # 네 방향 탐색해서 더 갈 수 있는 곳이 없으면 종료
        for _ in range(4):  # 네 방향 탐색
            new_i, new_j = oi + di[_], oj + dj[_]
            # mountain의 인덱스 범위를 벗어나지 않고, 방문체크 안되어있으면 현재 위치 보다 낮은지 확인
            if 0 <= new_i < N and 0 <= new_j < N and visited[new_i][new_j] == 0:
                # 갈 수 있는게 있으면 아래 과정 그대로 진행
                if mountain[oi][oj] > mountain[new_i][new_j]:
                    visited[oi][oj] = 1
                    find_route(new_i, new_j, left_k)
                    # 돌아오면 원복!
                    visited[oi][oj] = 0
        # 네 방향을 전부 확인했는데 더 갈 수 없으면????? return
        # 네 방향을 다 돌고 그냥 나왔으면
        visited[oi][oj] = 1 # 마지막 위치만 방문 처리해주고 종료
        for v in visited:
            cnt += v.count(1)
        max_cnt = max(max_cnt, cnt)
        return
    else:
        for _ in range(4):  # 네 방향 탐색
            new_i, new_j = oi + di[_], oj + dj[_]
            # mountain의 인덱스 범위를 벗어나지 않고, 방문체크 안되어있으면 현재 위치 보다 낮은지 확인
            if 0 <= new_i < N and 0 <= new_j < N and visited[new_i][new_j] == 0:
                # 현재 위치 보다 낮으면 현재 위치 방문 체크하고 이동
                if mountain[oi][oj] > mountain[new_i][new_j]:
                    visited[oi][oj] = 1
                    find_route(new_i, new_j, left_k)
                    # 돌아오면 원복!
                    visited[oi][oj] = 0
                # 만약 갈 수 없으면 깎아 보기(최소한으로)
                else:
                    for k in range(1, left_k+1):
                        # 최소한만 깎아보고 진행 가능하면 바로 진행하고 left_k = 0으로 만들면 됨
                        if mountain[oi][oj] > mountain[new_i][new_j] - k:
                            mountain[new_i][new_j] -= k
                            visited[oi][oj] = 1
                            left_k = 0
                            find_route(new_i, new_j, left_k)
                            # 돌아오면 원복
                            mountain[new_i][new_j] += k
                            visited[oi][oj] = 0
                            left_k = original_k
                            break       # for k
                    # k를 다 돌았는데도 갈 수 없으면 다른방향의 new_i,j 탐색해야됨





T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    # print(mountain)
    max_height = 0
    ans = 1
    result = []
    for m in mountain:
        max_height = max(max_height, max(m))
    # print(max_height)

    # for i, j : mountain[i][j] == max_height면 탐색 시작
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_height:
                visited = [[0] * N for _ in range(N)]
                cnt, max_cnt = 0, -float('inf')
                # 함수 적용 find_route()
                find_route(i, j, K)

                result.append(max_cnt)
                pass
                # print(f'ans:{ans}')

    # print(result)
    print(f'#{tc} {max(result)}')