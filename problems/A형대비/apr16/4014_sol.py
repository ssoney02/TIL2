def check_slope(row):
    tmp_cnt = 0
    for i in range(1, N):
        # 높이 차이에 변화가 생기면 tmp_cnt += 1씩 하다가, tmp_cnt < X인데 또 높이에 변화 생기면 건설 못함

        if row[]

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input.split())
    A = []
    cnt = 0