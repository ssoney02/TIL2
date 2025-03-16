def enq(idx):
    global last # 마지막 정점
    last += 1
    heap[last] = nums[idx]  # 마지막 정점에 nums[idx] 저장

    c = last    # 부모의 키 값과 비교하기 위해
    p = c//2    # 부모 정점 번호 계산

    while p != 0 and heap[p] > heap[c]:     # 부모가 있고, 부모 > 자식 인 경우(최소 힙 조건 위반)
        heap[p], heap[c] = heap[c], heap[p]
        c = p   # 현재 부모를 자식으로
        p = c // 2  # 부모의 부모 ( c = c//2가 됐음)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    idx = 0
    heap = [0] * (N+1)
    last = 0

    for i in range(N):
        enq(i)
    n = N
    ans = 0
    while n >= 1:
        n //= 2
        ans += heap[n]

    print(heap)
    print(f'#{tc} {ans}')