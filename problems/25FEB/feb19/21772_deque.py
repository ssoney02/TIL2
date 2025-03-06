from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    # print(q)
    q.rotate(-m)

    t = q.popleft()
    print(f'#{tc} {t}')