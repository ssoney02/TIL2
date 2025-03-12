delta = [[0, 1], [1, 0]]

def find_route(cnt, i, j, tmp_sum):
    global min_sum
    if tmp_sum > min_sum:   # 중간에 이미 min_sum보다 크면 그냥 멈추고 다른 방향 탐색(가지치기..)
        return
    if cnt == N*2-2:    # 어떤 상황이든 우/하 한 칸 씩 이동할 때 총 거리는 n*2 -2
        min_sum = min(tmp_sum, min_sum)
        return

    for d in delta:
        ni, nj = i + d[0], j + d[1]
        if 0 <= ni < N and 0 <= nj < N:    # 이동할 수 있으면
            tmp_sum += nums[ni][nj]
            find_route(cnt+1, ni, nj, tmp_sum)
            tmp_sum -= nums[ni][nj]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')
    init_sum = nums[0][0]
    find_route(0, 0, 0, init_sum)
    print(f'#{tc} {min_sum}')
