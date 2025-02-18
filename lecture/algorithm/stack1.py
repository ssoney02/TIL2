stack = [0] * 10
top = -1

print(f'original stack : {stack}')
top += 1
stack[top] = 3

print(f'new stack: {stack}')


########################################
top = -1
stack = [0] * 10

top += 1 # push(1)
stack[top] = 1

top += 1
stack[top] = 2 # push(2)

top += 1
stack[top] = 3 # push 3

# 세번 꺼냄
# 3, 2, 1 순 (역순)으로 꺼냄
top -= 1 #pop
print(stack[top+1])
top -= 1 #pop
print(stack[top+1])
top -= 1 #pop
print(stack[top+1])


#############
# 괄호 찾기..
txt = input()

top = -1
stack = [0] * 100

ans = 1 # 짝이 맞다고 가정 다르면 ans = 0으로 바꾸는 식
for x in txt:
    if x == '(': # 여는 괄호 push
        top += 1
        stack[top] = x
    # 중간에 공백같은게 끼여있을 수도 있어서.. else대신 elif 사용
    elif x == ')': # 닫는 괄호인 경우 (괄호 종류가 여러개면 x in ['(', '{',..] 이런식으로 해도됨)
        if top == -1: # 스택이 비어있으면
            ans = 0
            break # for x
        else:
            top -= 1
            # 소괄호만 있으므로 비교작업 생략
if top > -1: # 여는 괄호가 남아있으면
    ans = 0

print(ans)