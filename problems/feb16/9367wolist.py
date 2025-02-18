T = int(input())
for tc in range(1, T+1):
    n = int(input())
    c_list = list(map(int, input().split()))
    # print(c_list)
    max_cnt = 1
    cnt = 1
    for i in range(n-1):
        if c_list[i] >= c_list[i+1]: #감소하
            max_cnt = max(max_cnt, cnt)
            cnt = 1
        else:
            cnt += 1
            # print(f'증가중:{cnt}')
            # 증가할때마다 갱신하면 최대증가했을때 자동 갱신됨
            # 아니면 i가 마지막까지 계속 증가했을때에 대한 조건을 걸어주든가..
        if i == n-2:
            max_cnt = max(max_cnt, cnt)
            # print(f'max갱신:{max_cnt}')

    print(f'#{tc} {max_cnt}')