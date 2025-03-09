delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 상 우 하
pipe = {1: [0, 1, 2, 3], # 상우하좌
        2: [0, 2],  #상하
        3: [1, 3],  #우좌
        4: [2, 3],  #하좌
        5: [1, 2],  #우하
        6: [2, 3],  #우좌
        7: [0, 3]}  #상하
# 받아 줄 수 있는 파이프 체크
def check_pipe(oi, oj, ni, nj, tmp_k):
    flag = False
    if tunnel_map[oi][oj] == 1:
        # 현재 파이프가 1번 파이프면
        if tmp_k == 0 or 2:
            if tunnel_map[ni][nj] in [2, 5, 6]:
                flag = True
        elif tmp_k == 1:
            if tunnel_map[ni][nj] in [3, 6, 7]:
                flag = True
        else:
            if tunnel_map[ni][nj] in [3, 4, 5]:
                flag = True
    elif tunnel_map[oi][oj] == 2:
        if tmp_k == 0:
            if tunnel_map[ni][nj] in [1, 5, 6]:
                flag = True
        if tmp_k == 1:
            if tunnel_map[ni][nj] in [1, 4, 7]:
                flag = True
    elif tunnel_map[oi][oj] == 3:
        if tmp_k == 0:
            if tunnel_map[ni][nj] in [1, ]



    pass
def find_thief(oi, oj):
    if visited[oi][oj] == L:
        # 탈출 후 L시간에 도달했으면 함수 종
        return
    # 현재 위치 tunnel_map[oi][oj] 값을 키로 가지는 pipe[] 값 찾아
    for k in pipe[tunnel_map[oi][oj]]:
        # k: pipe의 value값 리스트를 순회
       ni, nj = oi + delta[k][0], oj + delta[k][1]
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
            # 범위 벗어나지 않고 방문한 적 없으면료
            # check_pipe로 받아 줄 수 있는 칸 인지 체
            check_pipe(oi, oj, ni, nj, k)
            visited[ni][nj] = visited[oi][oj] + 1
        print(ni, nj)

    pass

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    # N: 세로 크기 M: 가로 크기
    # [R,C]: 맨홀 뚜껑 위치
    # L: 탈출 후 소요된 시간
    # 파이프가 있으면 이동 가능 -> 파이프 번호에 따라 델타 탐색할 방향 다름(딕셔너리로 델타탐색 해볼 인덱스 지)
    # 파이프가 없으면..  map[i][j] == 0 이면 못감
    tunnel_map = [list(map(int, input().split())) for _ in range(N)]
    print(tunnel_map)
    visited = [[0]*M for _ in range(N)]
    visited[C][L] = 1
    print(visited)
    si, sj = C, L
