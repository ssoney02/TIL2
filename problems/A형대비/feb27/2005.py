T = int(input())
for tc in range(1, T+1):
    n = int(input())    # 삼각형의 크기 = 마지막 줄 수의 개수
    triangle = [[0]*(i+1) for i in range(n)]
    # print(triangle)
    triangle[0] = [1]
    # print(triangle)
    for i in range(1,n):
        for j in range(i+1):    # 한 줄의 길이: i+1
            if j == 0 or j == i:
                triangle[i][j] = 1
            else:
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    print(f'#{tc}')
    for _ in range(n):
        print(*triangle[_])

