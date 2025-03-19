def make_set(n):
    parents = [i for i in range(n+1)]
    ranks = [0] * (n+1)
    return parents, ranks

def find_set(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x

def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ranks[ref_x] < ranks[ref_y]:
        parents[ref_x] = ref_y
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_y] = ref_x
    else:
        parents[ref_y] = ref_x
        ranks[ref_x] += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    groups = list(map(int, input().split()))
    parents, ranks = make_set(N)
    res = []
    for i in range(M):
        union(groups[2*i], groups[2*i+1])
    for j in range(1, N+1):
        res.append(find_set(j))
    n_res = set(res)
    # print(n_res)
    print(f'#{tc} {len(n_res)}')
