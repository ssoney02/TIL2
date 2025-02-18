import sys
sys.stdin = open("1974input.txt", "r")
T = int(input())

for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    new_puzzle = list(map(list, zip(*puzzle)))

    result = 1
    for i in range(9):
        for j in range(8):
            # 가로 줄 확인
            if puzzle[i][j] in puzzle[i][j+1:]:
                result = 0
                break
            # 세로 줄 확인
            if new_puzzle[i][j] in new_puzzle[i][j+1:]:
                result = 0
                break
    # 3x3 씩 확인.....
    d1 = [-1, -1, -1, 0, 0, 1, 1, 1]
    d2 = [-1, 0, 1, -1, 1, -1, 0, 1]

    for m in range(3):
        for n in range(3):
            for r in range(8):
                ci = 1 + 3*m
                cj = 1 + 3*n
                # print(f'i: {ci}')
                # print(f'j: {cj}')
                if puzzle[ci][cj] == puzzle[ci+d1[r]][cj+d2[r]]:
                    result = 0
                    break

    print(f'#{tc} {result}')




