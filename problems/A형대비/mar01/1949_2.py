# import sys
# sys.stdin = open("1949input.txt", "r")
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def find_route(oi, oj, left_k, tmp_m):
    # oi,oj: 현재 위치
    # left_k: 남은 k
    global visited, max_cnt
    original_k = left_k
    # 종료 조건: 네 방향 탐색 다 했고, left_k까지 적용해봤는데, 더 갈 곳이 없으면 return
    # 깎을 필요 없이 계속 이동가능해도 마지막에 1까지 왔을때 주변을 깎아서 1보다 작아지면 더 진행가능!

    for _ in range(4):  # 네 방향 탐색
        new_i, new_j = oi + di[_], oj + dj[_]
        # mountain의 인덱스 범위를 벗어나지 않고, 방문체크 안되어있으면 현재 위치 보다 낮은지 확인
        if 0 <= new_i < N and 0 <= new_j < N and visited[new_i][new_j] == 0:
            # 현재 위치 보다 낮으면 현재 위치 방문 체크하고 이동
            if tmp_m[oi][oj] > tmp_m[new_i][new_j]:
                visited[oi][oj] = 1
                find_route(new_i, new_j, left_k, tmp_m)
                # 돌아오면 원복!
                visited[oi][oj] = 0
            # 만약 갈 수 없으면 깎아 보기(최소한으로)
            else:
                for k in range(1, left_k+1):
                    # 최소한만 깎아보고 진행 가능하면 바로 진행하고 left_k = 0으로 만들면 됨
                    # left_k == 0이면 어차피 안돌아감?????
                    if tmp_m[oi][oj] > tmp_m[new_i][new_j] - k:
                        tmp_m[new_i][new_j] -= k
                        # print(f'm:{tmp_m}')
                        visited[oi][oj] = 1
                        left_k = 0
                        find_route(new_i, new_j, left_k, tmp_m)
                        # 돌아오면 원복
                        tmp_m[new_i][new_j] += k
                        # print(f'm2:{tmp_m}')
                        visited[oi][oj] = 0
                        left_k = original_k
                        break       # for k
                # k를 다 돌았는데도 갈 수 없으면 다른방향의 new_i,j 탐색해야됨
                # else:   # 다 돌고 나왔는데 (_가 4인데 나왔으면 return)
        if _ == 3:
            cnt = 0
            # visited[oi][oj] = 1  # 마지막 위치만 방문 처리해주고 종료
            # print(f'v:{visited} \n')
            for v in visited:
                cnt += v.count(1)
            # print(f'cnt:{cnt}')
            max_cnt = max(max_cnt, cnt)
            return





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
                max_cnt = -float('inf')
                # 함수 적용 find_route()
                find_route(i, j, K, mountain)
                result.append(max_cnt)
                # print(f'ans:{ans}')

    # print(result)
    print(f'#{tc} {max(result)+1}')