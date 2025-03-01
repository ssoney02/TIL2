# import sys
# sys.stdin = open("1949input.txt", "r")
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def find_route(oi, oj, left_k):
    global ans
    original_k = left_k

    # 네 방향 탐색했을 때 (지형공사 더 못하고 k ==0 and) 더 이상 갈 곳이 없으면 return
    if left_k == 0:
        min_dh = float('inf')
        for _ in range(4):
            new_i = oi + di[_]
            new_j = oj + dj[_]
            if 0 <= new_i < N and 0 <= new_j < N :
                min_dh = min(min_dh, mountain[new_i][new_j])
        if min_dh >= mountain[oi][oj]:  # mountain[oi][oj]가 주변 중에 가장 낮으면
            result.append(ans)
            # print(visited)
            return                       # 함수 종료

    for _ in range(4):
        new_i = oi + di[_]
        new_j = oj + dj[_]

        if 0 <= new_i < N and 0 <= new_j < N :
            # 델타 인덱스가 mountain을 벗어나지 않으면 mountain[oi][oj]랑 크기비교
            if mountain[oi][oj] > mountain[new_i][new_j]:
                ans += 1
                # visited[new_i][new_j] = 1
                find_route(new_i, new_j, left_k)
                ans -= 1
                # visited[new_i][new_j] = 0
            else:   # 갈 수 없으면
                for k in range(1, left_k+1): # 최소한으로 깎아봄
                    if mountain[oi][oj] > mountain[new_i][new_j]-k:
                        mountain[new_i][new_j] -= k
                        left_k = 0
                        ans += 1
                        # visited[new_i][new_j] = 1
                        find_route(new_i, new_j, left_k)
                        # 원복!
                        mountain[new_i][new_j] += k
                        left_k = original_k
                        ans -= 1
                        # visited[new_i][new_j] = 0
                        break   # for k 더 많이 깎아볼 필요x..
                # 다 아봤는데 갈 수 없으면 다른 방향 탐색
                else:
                    min_dh = float('inf')
                    for _ in range(4):
                        new_i = oi + di[_]
                        new_j = oj + dj[_]
                        if 0 <= new_i < N and 0 <= new_j < N :
                            min_dh = min(min_dh, mountain[new_i][new_j])
                    if min_dh >= mountain[oi][oj]:  # mountain[oi][oj]가 주변 중에 가장 낮으면
                        result.append(ans)
                        # print(visited)
                        return
                    else:
                        continue




T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    # visited = [[0] * N for _ in range(N)]
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
                # 함수 적용 find_route()
                find_route(i, j, K)
                # print(f'ans:{ans}')
                # print(visited)

    # print(result)
    print(f'#{tc} {max(result)}')