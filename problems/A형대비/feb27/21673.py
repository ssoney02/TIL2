T = int(input())
for tc in range(1, T+1):
    stack = [0] * 100
    text = list(input())
    # print(text)
    result = []
    top = -1
    for t in text:
        if t in '1234567890':
            result.append(t)
        else:
            top += 1
            stack[top] = t

    while top >= 0:
        result.append(stack[top])
        top -= 1
    ans = ''.join(result)
    print(f'#{tc} {ans}')