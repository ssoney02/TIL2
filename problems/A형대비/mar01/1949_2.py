# import sys
# sys.stdin = open("1949input.txt", "r")
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]



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
                # 함수 적용 find_route()
                pass
                # print(f'ans:{ans}')

    # print(result)
    print(f'#{tc} {max(result)}')