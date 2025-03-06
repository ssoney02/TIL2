import sys
sys.stdin = open("1979input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]
    new_arr = list(map(list, zip(*arr)))
    # 흰색 부분에만 단어 들어갈 수 있음
    # arr[i][j]이랑 arr[i][j+1] 확인
    # for문 범위를 n 까지.. 하는데 마지막 j도 확인해서 넣어야됨
    # 만약 j+1 == n 이라면 arr[i][j] == 1이면 end point에 넣고 break
    # arr[i][0] == 1 이거나 0 -> 1 이면 1이 start point
    # 1 -> 0 이거나 맨끝값이 1이면 1이 end point


    def start(a, i, j, sp):
        if j == 0:
            if a[i][j] == 1:
                sp.append([i, j])
        else:
            if a[i][j - 1] == 0 and a[i][j] == 1:
                sp.append([i,j])
        return sp

    def end(a, i, j, ep):
        if j == n-1:
            if a[i][j] == 1:
                ep.append([i,j])
        else:
            if a[i][j] == 1 and a[i][j+1] == 0:
                ep.append([i,j])
        return ep


    c_cnt = 0
    r_cnt = 0
    for i in range(n):
        # start_point, end_point 초기화
        start_point = []
        end_point = []
        r_start_point = []
        r_end_point = []
        for j in range(n):
            # start_point:
            start_point = start(arr, i, j, start_point)
            end_point = end(arr, i, j, end_point)
            r_start_point = start(new_arr, i, j, r_start_point)
            r_end_point = end(new_arr, i, j, r_end_point)

        # print(f'sp:{start_point}')
        # print(f'ep:{end_point}')
        for m in range(len(start_point)):
            # start_point 길이랑 end_point 길이 동일
            L1 = end_point[m][1] - start_point[m][1] + 1
            # print(f'l:{L}')
            if L1 == k:
                c_cnt += 1

        for m in range(len(r_start_point)):
            L2 = r_end_point[m][1] - r_start_point[m][1] + 1
            if L2 == k:
                r_cnt += 1

    result = c_cnt + r_cnt
    print(f'#{tc} {result}')
    # col_cnt = cnt
    # # print(f'cc:{col_cnt}')
    #
    # new_arr = list(map(list, zip(*arr)))
    # # print(new_arr)
    # cnt = 0
    # for i in range(n):
    #     start_point = []
    #     end_point = []
    #     for j in range(n):
    #
    #     # print(f'nsp:{start_point}')
    #     # print(f'nep:{end_point}')
    #     for m in range(len(start_point)):
    #     # start_point 길이랑 end_point 길이 동일
    #         L = end_point[m][1] - start_point[m][1] + 1
    #     # print(f'l:{L}')
    #         if L == k:
    #             cnt += 1
    # row_cnt = cnt
    # # print(f'rc:{row_cnt}')
    # result = row_cnt + col_cnt
    # print(f'#{tc} {result}')






