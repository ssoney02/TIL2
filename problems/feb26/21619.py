T = int(input())
for tc in range(1, T+1):
    brackets = list(input())
    # print(brackets)
    stack = [0] * 100
    top = -1
    ans = 1
    for b in brackets:
        if b == '(':
            top += 1
            stack[top] = b
        # 닫는 괄호 인 경우
        # stack이 비어있으면 ans = -1하고 그냥 break
        # 비어있지않으면 stack에서 여는 괄호 하나 pop할 필요없이 그냥 top을 하나 줄이면됨..
        # 다음에 여는 괄호가 새로 들어와도 top += 1해서 새로 덮어씌우면 아무 상관x
        elif b == ')':  # 얘 else로 하면 fail뜸.. 괄호만 남긴댔는데..?
            if top == -1:
                ans = -1
                break
            else:
                top -= 1
    # brackets 다 돌았는데 stack에 여는괄호가 남아있으면 (top이 -1이 아니면) ans = -1
    if top != -1:
        ans = -1
    print(f'#{tc} {ans}')