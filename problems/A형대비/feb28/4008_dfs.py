def dfs(c_idx, c_cnt):     # 연산자 조합을 구해서 계산하는 함수
    if c_idx == 4:  # depth가 4까지 다 돌았으면 함수 중지
        return

    if c_cnt == 0:  # 연산자를 이미 다 썼으면 다음연산자 봐야됨
        dfs(c_idx+1)
        # 다음 c_cnt를 넘겨야....?
    else:
        top = -1
        while top <= len(numbers)-3:
            top += 1
            op1 = numbers[top]
            top += 1
            op2 = numbers[top]
            if c_cnt == 0:
                numbers[top] = op1 + op2
            elif c_cnt == 1:
                numbers[top] = op1 - op2
            elif c_cnt == 2:
                numbers[top] = op1 * op2
            elif c_cnt == 3:
                numbers[top] = int(op1 // op2)
            c_cnt -= 1






T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    # counts -> enumerate로 받으면 인덱스, 개수
    # counts idx에 따라 연산 달라짐
    # 연산자 조합 확인해서 계산
