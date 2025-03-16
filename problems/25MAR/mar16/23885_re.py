def enq(num):
    global last
    last += 1
    trees[last] = num
    c = last
    p = c // 2

    while p != 0 and trees[p] > trees[c]:
        trees[p], trees[c] = trees[c], trees[p]
        c = p
        p = c // 2  # 바뀐 c의 부모


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    trees = [0] * (N+1)
    last = 0    # 마지막 정점

    for num in nums:
        enq(num)
    print(trees)

