T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())        # N: N자리 이진수 K: 1의 개수
    bin_num = input()

    max_len = -float('inf')
    flag = 0
    # print(bin_num)
    for i in range(N):  # 싸피 이진수의 시작점 찾기
        cnt = 0
        if bin_num[i] == '1' and '1' in bin_num[i+1:]:  # 1로 끝나야되니까 뒤에 1있는지 확인
            for j in range(i+1, N):     # i+1부터 N까지 돌면서 1의 개수 cnt. K-1개가 되면 종료
                if bin_num[j] == '1':
                    cnt += 1
                    if cnt == K-1:  # 시작점 제외 K-1개 필요
                        flag = -1
                        tmp_len = j - i + 1
                        max_len = max(max_len, tmp_len)
                        break   # for j


    if flag == -1:
        res = max_len
    else:
        res = 0
    print(f'#{tc} {res}')
