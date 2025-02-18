T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # print(arr)

    points = []
    for i in range(n):
        for j in range(n):
            col_total = 0
            row_total = 0
            for k in range(n):
                col_total += arr[i][k]
                row_total += arr[k][j]
            total = col_total + row_total - arr[i][j] #가운데 i,j는 두번씩 들어감..
            points.append(total)
    # print(points)
    result = max(points) - min(points)

    print(f'#{tc} {result}')