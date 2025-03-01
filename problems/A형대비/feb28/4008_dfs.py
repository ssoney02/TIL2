def dfs(c_list, n_idx, result):     # 연산자 조합을 구해서 계산하는 함수
    # n_idx: numbers를 순회하는데 쓸 인덱스
    global max_sum, min_sum
    if n_idx == N:  # numbers를 다 돌았으면 계산 값 반환하고 중지
        max_sum = max(max_sum, result)
        min_sum = min(min_sum, result)
        return


    for op_idx, op_cnt in enumerate(c_list):
        if op_cnt == 0:     # 순열이니까 연산자 남아있는거 계속 처음부터 다 돌아야됨!
            continue
        tmp_res = result    # 진행 과정 도중 매번 연산할때마다 tmp_res에 넣어서 갱신
        if op_idx == 0:
            tmp_res += numbers[n_idx]
        elif op_idx == 1:
            tmp_res -= numbers[n_idx]
        elif op_idx == 2:
            tmp_res *= numbers[n_idx]
        elif op_idx == 3:
            if numbers[n_idx] == 0:
                # 분모가 0인 경우 예외처
                return
            tmp_res = int(tmp_res / numbers[n_idx])

        c_list[op_idx] -= 1     # 연산자 사용했으면 -1 해서 남은 개수 갱신
        # 갱신한 값들 넘김, 다음 숫자랑 계산시켜야됨
        dfs(c_list, n_idx+1, tmp_res)
        # 다 끝내고 돌아왔으면 원복시켜줘야됨
        c_list[op_idx] += 1
        # 다 돌았으면 끝나서 그 앞의 n_idx-1 이던 시점의 dfs 속으로 돌아옴


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    top = -1
    max_sum = -float('inf')
    min_sum = float('inf')
    # counts -> enumerate로 받으면 인덱스, 개수
    # counts idx에 따라 연산 달라짐
    # 연산자 조합 확인해서 계산
    init_idx = 1    # 1부터 돌릴것..!
    init_num = numbers[0]   # 첫번째 값을 초기 결과값으로(result) 넣어줄 것

    dfs(counts, init_idx, init_num)
    print(f'#{tc} {max_sum-min_sum}')

