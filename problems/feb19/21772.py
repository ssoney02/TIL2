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

    # print(queue)
    # cnt는 현재 이동 횟수 확인
    cnt = -1
    while cnt <= m-1 : # 확인..
        front = -1 # 초기화(다시 돌려면 -1부터 시작해야됨)
        while front != rear:
            front += 1
            cnt += 1    # cnt 번째 이동임
            if cnt == m:
                result = queue[front]
                break


    print(f'#{tc} {result}')



