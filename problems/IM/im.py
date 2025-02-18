T = int(input())

for tc in range(1, T+1):
    n = int(input()) # 배열의 크기
    original_arr = [list(map(int, input().split())) for _ in range(n)] # nxn 배열 만듦
    arr = [[0]*n for _ in range(n)]
    # print(original_arr)
    # for i in range(n):
    #     for j in range(n):
    #         using_arr[i][j] = original_arr[i][j]
    # print(f'ua:{using_arr}')
    # print(n)
    # print(original_arr)
    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 상, 우, 하, 좌 탐색

    # arr의 i,j 를 돌면서 탐색해야됨(출발위치)
    # 다 돌면서 한 번 이동할 때마다 cnt += 1
    # 이동하면서 원래 자리의 값은 501로 변환(최댓값)
    # 더 이상 갈 곳이 없으면(현재 높이보다 낮은 곳이 없으면) break -> cnt를 cnt_lst에 저장
    # i랑 j한번 바뀔 때마다 arr = original_arr로 초기화
    # max(cnt_lst) 출력
    # check_lst = []
    cnt_lst = [] # 모든 i,j에 대한 것
    for i in range(n): # 시작점i
        for j in range(n): # 시작점 j
            cnt = 1 # 시작 좌표 바뀔 때마다 갱신돼야됨
            # 이동할때마다 arr바꿔야되니까 arr 초기화
            for o in range(n):
                for p in range(n):
                    arr[o][p] = original_arr[o][p]

            # print(f'ua:{arr}')
            oi = i
            oj = j
            # print(f'arr:{arr}')
            # print(f'oi,oj: {oi},{oj}')
            while True:
                check_lst =[]
                for k in range(4): # 네 방향 확인
                    new_i = oi + delta[k][0]
                    new_j = oj + delta[k][1]
                    if 0 <= new_i < n and 0 <= new_j < n:
                        check_lst.append(arr[new_i][new_j])
                    # print(f'범위 안넘어가는거 확인:{check_lst}')
                if arr[oi][oj] < min(check_lst):  # 나보다 큰 애들 밖에없으면 갈곳 x
                    cnt_lst.append(cnt)
                    break
                else:   # 갈 곳 있는 경우
                    # check_lst의 min값을 불러와서
                    # print(check_lst)
                    # print(min(check_lst))
                    for k in range(4):
                        check_i = oi + delta[k][0]
                        check_j = oj + delta[k][1]
                        if 0 <= check_i < n and 0<= check_j < n:
                            if arr[check_i][check_j] == min(check_lst):
                                arr[oi][oj] = 501 # 501로 바꿔놓고
                                cnt += 1
                                oi = check_i
                                oj = check_j #이동하고
                                # check_lst = []
                                # print(f'갱신 arr:{arr}')
                                # break
    # print(f'cnt_lst:{cnt_lst}')
    print(f'#{tc} {max(cnt_lst)}')

