T = int(input())

for tc in range(1, T+1):
    n = int(input())    # 당근 수
    c_list = list(map(int, input().split())) # 당근 크기 리스트..
    cnt = 1     # 연속해서 커지지 않는 경우 구간의 최소길이 = 1
    cnt_lst = [1] # 연속하는게 없는 경우 최소 1이니까 미리 추가해둠..
    for i in range(n-1):
        if c_list[i] + 1 == c_list[i+1]:
            # i번째 당근 크기 +1 이 i+1번째 당근 크기이면..
            cnt += 1
        else:
            # 연속 증가하지 않으면..cnt의 max 값을 cnt = 1로 초기화
            # 직전까지 cnt값이 1보다 크면 cnt_list에 추가 후 초기화
            # 아니면 그냥 초기화..하면됨
            cnt = 1
        cnt_lst.append(cnt)
    print(cnt_lst)
    print(f'#{tc} {max(cnt_lst)}')

