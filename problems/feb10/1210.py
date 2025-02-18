import sys
sys.stdin = open("1210input.txt", "r")
# 어차피 밑에서 시작하면 한번 지나온 길은 다시 올 필요 없음
# 그냥 지나온 자리를 다 0으로 바꾸면 간단! (ladder에서)
T = 10
for tc in range(1, T+1):
    test_case = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]
    print(ladder)
    check_arr = [[0] * 100 for _ in range(100)]
    end_point = ladder[-1].index(2)
    # 밑에서부터 타고 올라감(tc 별 도착점 찾기)
    si = 99
    sj = end_point
    # print(end_point)
    # 윗쪽확인을 가장 마지막에 시킴 (좌우 이동 가능하면 먼저 해야하므로)
    di = [0, 0, -1]
    dj = [1, -1, 0]

    def check_ladder(i, j):
        # 왔던 지점 좌표 따로 저장

        # 얘로 저장하면 왜 None이 반환되는지 모르겠음................한방향으로 계속 가게 되지 않나..........?
        for k in range(3):
            check_i = i + di[k]
            check_j = j + dj[k]
            if 0 <= check_i < 100 and 0 <= check_j < 100:
                if check_arr[check_i][check_j] == 0:
                # if (check_i, check_j) != (old_i, old_j):
                    # 범위 벗어나는거 체크해야됨!!!!!!!!!!!!!!!!!!!!!!
                    # 왔던 곳으로 다시 가면 무한루프 걸림(예외처리)
                    if ladder[check_i][check_j] == 1:
                        # 새로운 좌표 중 값이 1인 곳으로 이동해야함
                        # i,j 값 갱신
                        check_arr[check_i][check_j] = 1
                        i = check_i
                        j = check_j
                        move = [i, j]
                        # print(result)
                        return move
                        break
    # initial_result = check_ladder(si, sj)
    # # print(f'a:{initial_result}')
    # # print(type(initial_result))
    # new_i = initial_result[0]
    # new_j = initial_result[1]
    while True:
        result = check_ladder(si, sj)
        print(result)
        si = result[0]
        sj = result[1]
        if si == 0:
            print(f'#{tc} {sj}')
            break





