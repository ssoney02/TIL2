from collections import deque

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())    # n: 화덕 크기, m : 피자 수

    c = list(map(int, input().split())) # 치즈양 m개..

    cheese = deque()
    i = m
    while i > 0:    # 피자가 다 없어질때까지..
        # 피자 넣으면 i -= 1
        for j in range(n):
            cheese.append(c[j])
        print(cheese)

        while 0 not in cheese:
            # 치즈양이 0인게 생기기 전까지 돌림
            if 0 in cheese:
                break
            cheese[]

