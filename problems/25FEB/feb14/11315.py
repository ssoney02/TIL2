import sys
sys.stdin = open("11315input.txt", "r")


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)] # 행 순회용 리스트
    row_arr = list(map(list, zip(*arr))) # 열 순회용 리스트 생
    cross_arr = list(map(list, zip(*row_arr))) #반대 대각선 순회용 리스트
    r_cross_arr = list(map(list, zip(*cross_arr)))

    # result = 'NO'
    # 델타 행 -> 열 -> 왼쪽 대각선 -> 오른쪽 대각선 순으로 돌
    di = [0, 0, 0, 0, -2, -1, 1, 2, -2, -1, 1, 2, -2, -1, 1, 2]
    dj = [-2, -1, 1, 2, 0, 0, 0, 0, -2, -1, 1, 2, 2, 1, -1, -2]
    # di, dj는 4개씩 끊어서 확인!
    # k를 0부터 16까지 돌리면서
    # k가 0, 4, 8, 12일때마다 cnt = 1로 초기화
    # if cnt == 5가 되면 result = 'YES'하고 바로 break
    # i + di 나 j + dj 중에 범위 벗어나는거 있으면 바로 break해야됨
    result = 'NO'
    for i in range(n):
        if result == 'YES':
            break
        for j in range(n):
            if arr[i][j] == 'o':
                for k in range(16):
                    if k in [0, 4, 8, 12]:
                        cnt = 1

                    if 0 <= i+di[k] < n and 0 <= j+dj[k] < n:
                        if arr[i+di[k]][j+dj[k]] == 'o':
                            cnt +=1
                    if cnt == 5:
                        result = 'YES'
                        break

    print(f'#{tc} {result}')










