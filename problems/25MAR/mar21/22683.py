# 현재 방향 -> 0: 상, 1: 우, 2: 하, 3: 좌
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 이동은 전진만 가능! 방향에 따라 전진할 델타 다름, 회전은 회전만 가능..
def change_dir(tmp_d):
    global cnt
    if tmp_d == 3:
        tmp_d = 0
    else:
        tmp_d += 1
    cnt += 1
    return tmp_d




def rccar(oi, oj, tmp_k, tmp_d):
    global min_cnt, cnt, flag

    if min_cnt < cnt:
        return
    if field[oi][oj] == 'Y':  # 목적지에 도착했으면 min_cnt 갱신하고 종료
        flag = 0
        min_cnt = min(min_cnt, cnt)
        return

    # for d in range(4):
    ni, nj = oi + delta[tmp_d][0], oj + delta[tmp_d][1]
    if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:  # 범위 벗어나지 않고, 방문한적 없으면
        # field[ni][nj] == 'G'면 그냥 이동 가능
        # field[ni][nj] == 'T'면 K값 체크
        if field[ni][nj] == 'T':
            if tmp_k > 0:  # 나무 인데 tmp_k가 남아있으면 진행 가능, 아니면 진행 불가
                cnt += 1  # 진행하면서 cnt += 1
                visited[oi][oj] = 1
                rccar(ni, nj, tmp_k - 1, tmp_d)
                cnt -= 1  # 원복
                visited[oi][oj] = 0
        else:
            cnt += 1
            visited[oi][oj] = 1
            rccar(ni, nj, tmp_k, tmp_d)
            cnt -= 1
            visited[oi][oj] = 0
    # 갈 수 없으면 방향 바꿔서 진행
    # 방향 바꾸면 cnt += 1
    rccar(oi, oj, tmp_k, change_dir(tmp_d))
    # 방향을 계속 바꿔봤는데 진행할 수 없으면.. (네 방향 다 봤음..
    cnt -= 1


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    field = [input() for _ in range(N)]
    print(field)
    cnt = 0
    min_cnt = float('inf')
    visited = [[0] * N for _ in range(N)]
    flag = -1
    # # 출발지: X, 목적지: Y, 이동가능 영역: G, 나무: T
    for l in range(N):
        for m in range(N):
            if field[l][m] == 'Y':
                ei, ej = l, m
                break
    # 0: 상, 1: 우, 2: 하, 3: 좌
    # if ei - oi == 0:
        # if ei - oj > 0 : tmp_d = 1
        # if ei - oj < 0: tmp_d = 3
    # if ej - oj == 0:
    #     if ei - oi > 0 : tmp_d = 2
    #     if ei - oi < 0 : tmp_d = 0
    # if ei - oi >0 and ej - oj > 0 : tmp_d = 1 or 2인게 유리
    # if ei - oi >0 and ej - oj < 0 : tmp_d = 1 or 3 유리
    # if ei - oi <0 and ej - oj >0 : tmp_d = 0 or 1인게 유리
    # if ei - oi <0 and ej - oj < 0 : tmp_d =
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                # 항상 위를 바라보는 상태로 rc카 조작 시작
                rccar(i, j, K, 0)
                break  # 출발지 하나니까 돌고나면 그냥 break해주면 됨

    if flag == -1:
        min_cnt = -1
    print(min_cnt)