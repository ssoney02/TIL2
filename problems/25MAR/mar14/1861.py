import sys
sys.stdin = open('1861input.txt', 'r')
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
def find_room(oi, oj, cnt):
    global max_cnt
    # 이동 가능 조건
    # ni, nj가 범위를 안벗어 나고
    # room[oi][oj] + 1 == room[ni][nj]
    # visited == 0 이면

    # 종료조건: 이동 불가능하면!
    for d in range(4):
        ni, nj = oi + delta[d][0], oj + delta[d][1]
        if 0 <= ni < N and 0 <= nj < N and room[oi][oj] + 1 == room[ni][nj] and visited[ni][nj] == 0:
            # 이동 가능!
            visited[ni][nj] = 1
            cnt += 1
            find_room(ni, nj, cnt)
            # 원복
            visited[ni][nj] = 0
            cnt -= 1
            break
    else:
        max_cnt = max(cnt, max_cnt)
        return
def find_min():
    for i in range(N):
        if
        j = room.index(min(room))

    if visited[i][j] == 0:
        return i, j
    else:
        room[i][j] = N ** 2
        find_min()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    max_cnt = -float('inf')
    max_res = -float('inf')
    start_point = float('inf')
    # 값이 작은 것 부터 탐색 시작하면.. 가장 긴 거리 부터 확인 가능..
    # 그 다음 수들은 어차피 같은 길을 갈거라 더 짧아짐.. visited 원복 안하고!
    while 0 not in visited:
        si, sj = find_min()
        visited[si][sj] = 1
        find_room(si, sj, 1)
        if max_cnt >= max_res:
            start_point = min(start_point, room[si][sj])
            max_res = max_cnt

    print(f'#{tc} {start_point} {max_res}')