import sys
sys.stdin = open("1215input.txt", "r")

T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    print(arr)
    cnt = 0
    for i in range(8):
        for j in range(8):
            if 0 <= j + n < 9:
                word_col = []
                word_row = []
                for m in range(n):
                    word_col.append(arr[i][j+m])
                    word_row.append(arr[j+m][i])

                for k in range(n // 2):
                    if word_col[k] != word_col[n - 1 - k]:
                        break
                else:
                    cnt += 1
                # print(f'cnt1:{cnt}')
                # for else: for문에서 break 걸리지 않으면 else진행
                for k in range(n // 2):
                    if word_row[k] != word_row[n - 1 - k]:
                        break
                else:
                    cnt += 1
                # print(f'cnt2:{cnt}')

    print(f'#{tc} {cnt}')