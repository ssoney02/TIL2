from collections import deque

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())  # n: 화덕크기, m: 피자 수
    c = list(map(int, input().split()))
    cheese = deque()  # 화덕
    idx_lst = deque()
    # 화덕에 피자 넣기 (처음 n개)
    for _ in range(n):
        cheese.append(c[_])
        idx_lst.append(_)   # 인덱스도 같이 돌려야..


    # rotate -> popleft하고 반환값을 append
    cnt = n - 1  # 처음에 넣는 피자 인덱스의 최대값
    while True:  # 확인!!!!!!!!
        if cnt == m - 1 and cheese.count(0) == n - 1:   # 더 이상 넣을 피자도 없고, 화덕안에 들어있는 피자도 하나 빼고 다 0이면
            while cheese[0] == 0:
                c_t = cheese.popleft()
                cheese.append(c_t)
                i_p = idx_lst.popleft()
                idx_lst.append(i_p)

            num = idx_lst[0] + 1
            print(f'#{tc} {num}')
            break  # while문에 대한 break

        cheese[0] //= 2  # 입구 자리에있는것부터 2씩 나눔

        # cheese[0] == 0 이 되면 바로 break하고 빠져나와서 cheese[0]에 새 피자 넣어야됨
        if cheese[0] == 0:  # 새로운 피자 넣기
            cnt += 1  # cnt 하나 늘려서 c[cnt]를 cheese[0]에 넣으면 남아있는 피자 하나씩 넣을 수 있음
            if cnt == m:    # 더 넣을 피자가 없으면! 들어있는 애들이 마지막 하나가 남을때까지 돌려야됨
                cnt = m - 1  # cnt = n-1로 바꾸고 그냥 pass..
            else:
                cheese[0] = c[cnt]
                idx_lst[0] = cnt  # cnt는 다음에 넣어야될 c의 인덱스 값
        # 넣었으면 또 돌리면 됨..
        c_t = cheese.popleft()
        cheese.append(c_t)
        i_t = idx_lst.popleft()
        idx_lst.append(i_t)