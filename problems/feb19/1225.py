from collections import deque

T = 10
for tc in range(1, T+1):
    case = int(input())
    q = deque(map(int, input().split()))
    while 0 not in q:
        for n in range(1, 6):
            t = q.popleft() - n
            if t <= 0:
                t = 0
                q.append(t)
                break
            q.append(t)

        if 0 in q:
            break
    # print(q)
    result = []
    for i in range(len(q)):
        result.append(str(q.popleft()))
    f_result = ' '.join(result)
    print(f'#{tc} {f_result}')