T = int(input())
for tc in range(1, T+1):
    text = list(input().split())
    # print(text)
    stack = ['a'] * 1000
    top = -1

    for t in text:
        if t == '.':
            result = int(stack[top])
            #break # 확인! 연산
        elif t not in '+-*/':
            top += 1
            stack[top] = int(t)
        else:
            if top <= 0:
                result = 'error'
                break   # for t
            else:
                op2 = stack[top]
                top -= 1
                op1 = stack[top]
                top -= 1
                if t == '+':
                    top += 1
                    stack[top] = op1 + op2
                elif t == '-':
                    top += 1
                    stack[top] = op1 - op2
                elif t == '/':
                    top += 1
                    stack[top] = op1 / op2
                elif t == '*':
                    top += 1
                    stack[top] = op1 * op2


    if '.' not in text:
        result = 'error'
    if top != 0:
        result = 'error'
    print(f'#{tc} {result}')





