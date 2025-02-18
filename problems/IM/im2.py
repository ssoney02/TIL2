import copy
T = int(input())

for tc in range(1, T+1):
    n = int(input()) # 배열의 크기
    original_arr = [list(map(int, input().split())) for _ in range(n)] # nxn 배열 만듦

    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 상, 우, 하, 좌 탐색
    arr = copy.deepcopy(original_arr)
    cnt_lst = [] # 모든 i,j에 대한 것

    for i in range(n): # 시작점i
        for j in range(n): # 시작점 j
            cnt = 1 # 시작 좌표 바뀔 때마다 갱신돼야됨
            # 이동할때마다 arr바꿔야되니까 arr 초기화
            arr = copy.deepcopy(original_arr)
            oi = i
            oj = j

            while True:
                check_lst =[]
                for k in range(4): # 네 방향 확인
                    new_i = oi + delta[k][0]
                    new_j = oj + delta[k][1]
                    if 0 <= new_i < n and 0 <= new_j < n:
                        check_lst.append(arr[new_i][new_j])

                if arr[oi][oj] < min(check_lst):  # 나보다 큰 애들 밖에없으면 갈곳 x
                    cnt_lst.append(cnt)
                    break
                else:   # 갈 곳 있는 경우
                    # check_lst의 min값을 불러와서
                    for k in range(4):
                        check_i = oi + delta[k][0]
                        check_j = oj + delta[k][1]
                        if 0 <= check_i < n and 0<= check_j < n:
                            if arr[check_i][check_j] == min(check_lst):
                                arr[oi][oj] = 501 # 501로 바꿔놓고
                                cnt += 1
                                oi = check_i
                                oj = check_j #이동하고
                                break

    print(f'#{tc} {max(cnt_lst)}')