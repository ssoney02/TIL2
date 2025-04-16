#4014. 활주로 건설
def cnt_line(ground):
    global cnt, N, X
    for i in range(N):
        check = ground[i].count(ground[i][0])
        if check == N:
            cnt += 1
        elif any(ground[i][N - X] != ground[i][k] for k in range(N-X+1, N-1)):
            continue
            # 끝에 X개 확인했을 때, 값이 다른게 있으면 그냥 break

        else:
            # tmp_cnt = 0
            for j in range(N):
                if j < N-X:
                    if abs(ground[i][j+1] - ground[i][j]) > 1:
                        # 높이차가 1보다 큰게 있으면 그냥 건설 못함 -> 다음 줄로 이
                        break   # for j
                    elif ground[i][j+1]-ground[i][j] == 1:
                        # 올라가는 경우면
                        # [i][j-X+1]부터 [i][j]까지 높이 동일해야됨
                        # 마지막 X개 칸은.. 증가하는 경우만 검사..
                        if any(ground[i][k] != ground[i][j] for k in range(j-X+1,j)):
                            break
                    elif ground[i][j] - ground[i][j+1] == 1:
                        # 내려가는 경우면
                        # [i][j+1]부터 [i][j+X]까지 높이 동일해야됨
                        if any(ground[i][k] != ground[i][j+1] for k in range(j+1,j+X+1)):
                            break
                else:
                    if abs(ground[i][j] - ground[i][j-1]) > 1:
                        # 높이차가 1보다 큰게 있으면 그냥 건설 못함 -> 다음 줄로 이
                        break  # for j
                    elif ground[i][j] - ground[i][j-1] == 1:
                        if any(ground[i][k] != ground[i][j] for k in range(j - X + 1, j)):
                            break
            else:
                # 다 통과했으면
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())    # N: 지도 한 변 크기 , X: 경사로 길이

    arr = [list(map(int,input().split())) for _ in range(N)]
    print(arr)
    cnt = 0

    cnt1 = cnt_line(arr)
    # print(cnt1)
    arr_rotate = list(map(list, zip(*arr)))
    # print(arr_rotate)
    res = cnt_line(arr_rotate)
    print(f'#{tc} {res}')



