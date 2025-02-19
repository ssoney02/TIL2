
T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())    # n: 화덕 크기, m : 피자 수

    c_lst = list(map(int, input().split())) # 치즈양 m개..
    c_copy = c_lst

    cheese = []
    # i = m
    idx_lst = []
    cnt = n-1 # 초기에 피자 인덱스: 0~n-1까지 들어감
    # 그 다음부터는 하나씩 커지면서 idx_lst[빠지는 위치] = cnt+1
    # while i > 0:    # 피자가 다 없어질때까지..
        # 피자 넣으면 i -= 1
    for j in range(n):
        cheese.append(c_lst[j])
    # print(cheese)

    for k in range(n):
        idx_lst.append(k) # 처음에 n개 피자 들어감
        # 그 다음에 들어가는 애들 부터는 idx_lst[빠지는 인덱스] = (cnt+=1)
        # 하나빠지면 (새로 들어가야되면) cnt += 1 시키고
        # idx_lst[빠지는 인덱스] = cnt

    flag = 0
    c = 0
    while True:
        # 화덕에서 돌리기 전에 넣은 피자의 치즈양의 인덱스? 따로 카피 떠놓고 (위치는 어차피 고정이니까..)
        # 치즈양이 0인게 생기기 전까지 돌림

        while c <= n-1:
            cheese[c] //= 2
            if 0 in cheese:  # 꺼내야 될 피자가 생기
                # print(cheese)
                cnt += 1
                if cnt == m-1:
                    # 더 넣을 피자가 없음
                    # max로 바로 구해도 되나..? 안될듯 얘문제같음...!!!!
                    while cheese.count(0) == n-1:
                        cheese[c] //= 2 # 마지막 화덕 돌리기.. 다 차있는 상태
                        c += 1
                        # 0 나오는건 그냥 0으로 냅두면
                        if c == n:
                            c = 0
                    # 다 돌렸으면
                    num = idx_lst[cheese.index(max(cheese))] + 1
                    flag = 1
                    break
                n_idx = cheese.index(0) # 빼야할 피자 인덱스 찾음
                # cheese[n_idx] = c[cnt]랑, idx_lst[n_idx] = cnt
                cheese[n_idx] = c_lst[cnt]
                idx_lst[n_idx] = cnt
                c += 1
                break
            c +=1

        if c == n:
            c = 0

        if flag == 1:
            break

    print(f'#{tc} {num}')
