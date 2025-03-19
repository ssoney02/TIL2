def calculate(res):
    global M, cnt, min_cnt
    if cnt >= min_cnt:  # 최소 연산 횟수니까 넘어가면 그냥 리턴
        return
    if res == M:        # M이 만들어졌으면 종료
        min_cnt = min(cnt, min_cnt)
        return
    if res > 1000000 or res <= 0:   # 연산결과는 1000000이하 & 자연수
        return

    for k in range(4):
        if k == 0:
            res -= 10
            cnt += 1
            calculate(res)
            res += 10
            cnt -= 1
        elif k == 1:
            res += 1
            cnt += 1
            calculate(res)
            res -= 1
            cnt -= 1
        elif k == 2:
            res -= 1
            cnt += 1
            calculate(res)
            res += 1
            cnt -= 1
        elif k == 3:
            res *= 2
            cnt += 1
            calculate(res)
            res /= 2
            cnt -= 1



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    min_cnt = float('inf')
    cnt = 0
    calculate(N)

    print(f'#{tc} {min_cnt}')
