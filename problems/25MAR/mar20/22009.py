def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V+1: 노드 수, E: 간선 수
    edges = []
    for _ in range(E):
        n1, n2, weight = map(int, input().split())
        edges.append((n1, n2, weight))

    edges.sort(key=lambda x: x[2])  # 가중치 기준 오름차순 정렬
    parents = [i for i in range(V + 1)]

    cnt = 0  # 현재까지 선택한 간선 수
    res = 0  # 가중치 합

    for u, v, w in edges:
        if find_set(u) != find_set(v):
            union(u, v)
            cnt += 1
            res += w

            if cnt == V:
                break
    print(f'#{tc} {res}')
