def pre_order(T):
    if T:       # 0이 아니면
        res.append(T)
        pre_order(left[T])
        pre_order(right[T])

V = int(input())
trees = list(map(int, input().split()))
par = [0] * (V+1)
left = [0] * (V+1)
right = [0] * (V+1)
for i in range(V-1):
    p, c = trees[2*i], trees[2*i + 1]
    par[c] = p
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
print(par)
# print(left)
# print(right)
res = []

pre_order(1)
print(*res)