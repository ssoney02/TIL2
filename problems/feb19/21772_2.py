T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    queue = [0] * n

    front = rear = -1
    # 큐에 삽입
    while rear < n-1 :
        rear += 1
        queue[rear] = num[rear]

    for cnt in range(m+1):
