#4014. 활주로 건설
def cnt_line():
    pass

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())    # N: 지도 한 변 크기 , X: 경사로 길이

    ground = [list(map(int,input().split())) for _ in range(N)]
    print(ground)
    cnt = 0
    for i in range(N):
        check = ground[i].count(ground[i][0])
        if check == N:
            cnt += 1
        else:
            tmp_cnt = 0
            for j in range(N-1):
                if abs(ground[i][j+1] - ground[i][j]) > 1:
                    # 높이차가 1보다 큰게 있으면 그냥 건설 못함 -> 다음 줄로 이
                    break   # for j
                elif ground[i][j+1]-ground[i][j] == 1:
                    # 올라가는 경우면
                    # [i][j-X+1]부터 [i][j]까지 높이 동일해야됨
                elif ground[i][j] - ground[i][j+1] == 1:
                    # 내려가는 경우면
                    # [i][j+1]부터 [i][j+X]까지 높이 동일해야됨


            #S2