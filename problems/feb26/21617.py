T = int(input())
for tc in range(1, T+1):
    text = list(input())
    # print(text)
    top = -1
    ans = 1
    stack = [0] * 100
    for t in text:
        if t in ['{', '(']:
            top += 1
            stack[top] = t
        elif t in ['}', ')']:
            if t == '}':
                if stack[top] == '{':
                    top -= 1    # pop
                else:
                    ans = 0
                    break
            if t == ')':
                if stack[top] == '(':
                    top -= 1    # pop
                else:
                    ans = 0
                    break
    if top != -1:
        ans = 0
    print(f'#{tc} {ans}')