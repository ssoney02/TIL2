def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return
    # 작은 쪽으로 몰아주
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append((n1, n2, w))

    edges.sort(key=lambda x:x[2])
    parents = [i for i in range(V+1)]
    cnt, w_sum = 0, 0
    for s,e,weight in edges:
        if find_set(s) != find_set(e):
            union(s,e)
            cnt += 1
            w_sum += weight

            if cnt == V:
                break

    print(f'#{tc} {w_sum}')