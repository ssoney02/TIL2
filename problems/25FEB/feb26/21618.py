T = int(input())
for tc in range(1, T+1):
    text = list(input())
    stack = [0] * 100000    # 문자열 길이: 1000이내............
    # t를 돌면서 stack[top]이랑 계속 비교
    # 일치하면 top -= 1
    # 아니면 top += 1 stack[top] = t
    # ans = top + 1
    top = -1
    for t in text:
        if stack[top] != t:
            top += 1
            stack[top] = t
        elif stack[top] == t:
            top -= 1

    ans = top + 1
    print(f'#{tc} {ans}')