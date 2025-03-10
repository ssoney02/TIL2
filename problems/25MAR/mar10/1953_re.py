
delta = [[-1, 0], [0, -1], [0, 1], [1, 0], ]  # 상 좌 우 하
# 델타를 0:상, 1:좌, 2:우, 3:하 => 0이 pipe의 value값에 있으면
# for val in pipe[tunnel_map[oi][oj]] : 3- val in pipe[tunnel_map[ni][nj]]이면 이동 가능
pipe = {1: [0, 1, 2, 3], # 상우하좌
        2: [0, 3],  #상하
        3: [2, 1],  #우좌
        4: [0, 2],  #상우
        5: [2, 3],  #우하
        6: [1, 3],  #좌하
        7: [0, 1]}  #상좌

# 받아 줄 수 있는 파이프 체크
def check_pipe(oi, oj, ni, nj, tmp_k):
    # global flag
    flag = False
    if tunnel_map[oi][oj] == 1:
        if tunnel_map[ni][nj] == 1:
            flag = True
        else:
            if tmp_k == 0:
                if tunnel_map[ni][nj] in [2,5,6]:
                    flag = True
            elif tmp_k == 1:#좌
                if tunnel_map[ni][nj] in [3, 4 ,5]:
                    flag = True
            elif tmp_k == 2: # 우
                if tunnel_map[ni][nj] in [3, 6, 7]:
                    flag = True
            else:
                if tunnel_map[ni][nj] in [2, 4, 7]:
                    flag = True

    else:
        if (3 - tmp_k) in pipe[tunnel_map[ni][nj]]:
            flag = True
            return flag
    return flag

def find_thief(si, sj):

    # 현재 위치 tunnel_map[oi][oj] 값을 키로 가지는 pipe[] 값 찾아
    # print(f'형태확인:{pipe[tunnel_map[oi][oj]]}')
    q = []
    q.append([si, sj])
    while q:
        t = q.pop(0)
        if visited[t[0]][t[1]] == L:
            return
        # print(t)
        for k in pipe[tunnel_map[t[0]][t[1]]]:  # 갈 수 있는 모든 방향에 대해
            ni, nj = t[0] + delta[k][0], t[1] + delta[k][1]
            if 0 <= ni < N and 0 <= nj < M and tunnel_map[ni][nj] != 0 and visited[ni][nj] == 0:
                flag = check_pipe(t[0], t[1], ni, nj, k)
                if flag == True:    # 진행 가능 하면
                    q.append([ni, nj])
                    visited[ni][nj] = visited[t[0]][t[1]] + 1



T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    # N: 세로 크기 M: 가로 크기
    # [R,C]: 맨홀 뚜껑 위치
    # L: 탈출 후 소요된 시간
    # 파이프가 있으면 이동 가능 -> 파이프 번호에 따라 델타 탐색할 방향 다름(딕셔너리로 델타탐색 해볼 인덱스 지)
    # 파이프가 없으면..  map[i][j] == 0 이면 못감
    tunnel_map = [list(map(int, input().split())) for _ in range(N)]
    # print(tunnel_map)
    visited = [[0]*M for _ in range(N)]
    visited[R][C] = 1
    # print(visited)
    # si, sj = C, L
    find_thief(R, C)
    # for v in visited:
    #     print(v)
    ans = N*M
    for v in visited:
        ans -= v.count(0)
    print(f'#{tc} {ans}')