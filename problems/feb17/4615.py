T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    play = [list(map(int, input().split())) for _ in range(m)] # play[0]:i, play[1]:j, play[2]:돌색깔(흑:1, 백:1)
    # 내가 돌을 놨는데
    # 내 돌에서 delta 순회햇을때 상대편 돌이 잇으면.. 그 방향만큼 *k 배 해서 돌았을때(판을 다 돌아야되나...?)
    # 내 돌이 있으면... 내 돌로 바꾸기 가능.
    # 놓을 수 없는 곳은 입력으로 주지 않음!

    # 초기 배열
    arr = [[0]*n for _ in range(n)]
    arr[n//2-1][n//2-1], arr[n//2-1][n//2], arr[n//2][n//2-1], arr[n//2][n//2] = 2, 1, 1, 2
    print(arr)
    flag = True
    for _ in range(m):
        new_i = play[_][1]-1
        new_j = play[_][0]-1

        arr[new_i][new_j] = play[_][2]
        if play[_][2] == 1: # 새로 놓은 돌이 흑돌일 때
            for k in range(len(d)):
                if flag == False:
                    flag = True
                    break
                if 0 <= new_i+d[k][0] <n and 0<= new_j+d[k][1]< n:
                    if arr[new_i+d[k][0]][new_j+d[k][1]] == 2: # 델타 순회 중 상대 돌이 있으면
                        b = 2
                        while 0 <= new_i+b*d[k][0] < n and 0 <= new_j+b*d[k][1] < n:
                            # 내 돌이 있으면
                            if arr[new_i + b*d[k][0]][new_j+b*d[k][1]] == 1:
                                for c in range(b):
                                    arr[new_i + c*d[k][0]][new_j+c*d[k][1]] = 1 # 나 부터 다른 흑돌 사이에 있는 값들을 흑돌로 갱신
                                print(f'놓음: {arr}')
                                flag = False
                            b += 1
                    else:
                        arr[new_i][new_j] = 0
        if play[_][2] == 2:  # 새로 놓은 돌이 백돌 일 때
            for k in range(len(d)):
                if flag == False:
                    flag = True
                    break
                if 0 <= new_i + d[k][0] < n and 0 <= new_j + d[k][1] < n:
                    if arr[new_i + d[k][0]][new_j + d[k][1]] == 1:  # 델타 순회 중 상대 돌이 있으면
                        b = 2
                        while 0 <= new_i + b * d[k][0] < n and 0 <= new_j + b * d[k][1] < n:
                            # 내 돌이 있으면
                            if arr[new_i + b * d[k][0]][new_j + b * d[k][1]] == 2:
                                for c in range(b):
                                    arr[new_i + c * d[k][0]][new_j + c * d[k][1]] = 2  # 나 부터 다른 흑돌 사이에 있는 값들을 백돌로 갱신
                                print(f'놓음: {arr}')
                                flag = False
                            #else: # 내 돌이 없으면 그냥 못놓음..  안주어짐..
                            b += 1
                    else:
                        arr[new_i][new_j] = 0
            # 찾아서 갱신했으면 break하고 다음 play 돌아야됨
    print(arr)
    b_cnt = 0
    w_cnt = 0
    for a in arr:
        b_cnt += a.count(1)
        w_cnt += a.count(2)

    print(f'#{tc} {b_cnt} {w_cnt}')