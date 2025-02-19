T = int(input())

for tc in range(1, T+1):
    a, b = input().split()
    # print(a)
    # print(b)
    cnt = 0
    a_lst = list(a)
    b_lst = list(b)
    i = 0
    j = 0   # 일단 j는 0에서 시작
    cnt = 0
    while i < len(a):
        # i,j는 시작점에 대한 것!
        if a_lst[i] == b_lst[j]:    # a[i]를 돌다가 b[0]이랑
            n_i = i + 1             # 일치하는게 있으면 i, j하나씩 늘려서 다음도 일치하나 확인
            n_j = j + 1
            while n_j < len(b):     # b가 다 끝날때까지 확인
                if n_i >= len(a):
                    cnt += n_j
                    i = n_i
                    break
                if a_lst[n_i] == b_lst[n_j]:
                    if n_j == len(b)-1:         # 끝까지 다 돌았으면
                        cnt += 1
                        i = i + len(b)
                        j = 0
                        break
                    n_i += 1
                    n_j += 1

                else :  # b를 돌다가 일치하지 않는게 나오면 i = i+1로 이동, j =0으로 초기화
                    i += 1
                    j = 0
                    cnt += 1 # 중간에 바뀌면 cnt +=1
                    break
                # 끝까지 다 일치하면 cnt += 1

        else:      # 일치하지 않으면 그냥 cnt
            cnt += 1
            i += 1
            j = 0

    print(f'#{tc} {cnt}')



