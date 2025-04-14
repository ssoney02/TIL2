# 5656.벽돌깨기
# 구슬 발사횟수: n
# 벽돌 -> W * H 배열로 주어짐
#   0: 빈공간
#   1~9 숫자로 주어짐
#   구슬로 벽돌 치면 상하좌우로 벽돌 숫자 -1 칸 만큼 같이 제거
#   아래에 빈공간 생기면 아래로 떨어짐

# 최대한 많은 벽돌을 깨뜨렸은 경우, 남은 벽돌의 개수!
# 맨 위에 있는 벽돌만 깰 수 있음
# -> 맨 위 벽돌 하나씩 돌아가면서 먼저 깨보고, 각각 남은 벽돌 수 가 최소면 갱신

delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]   # 상,우,하,좌 네 방향
T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split()) # N: 구슬 쏘는 횟수, W: 가로 벽돌 수, H: 세로 벽돌 수
    bricks = [list(map(int, input().split())) for _ in range(H)]

    print(bricks)
    # 제일 위에 있는 벽돌들 구하기 (시작점)
    start_idx = []
    for i in range(H):
        # 0이 아닌 다른 숫자가 bricks[i]에 있는 경우 => any!!
        # if any(bricks[i][j] != 0 for j in range(W)):
        #     start_idx.append((i, j))
        #     break   # for i
        for j in range(W):
            if bricks[i][j] != 0:
                start_idx.append((i,j))
        if start_idx:
            # for i -> i 행의 0이 아닌 시작값은 다 저장하고 그 밑의 줄은 탐색x
            # 시작점 저장했으면 탐색 중단. 맨 윗 줄에 있는 것부터만 깰 수 있음
            break


    while N > 0:
        # 한 번 쏠 때 마다 N -= 1

        N -= 1

    print(start_idx)