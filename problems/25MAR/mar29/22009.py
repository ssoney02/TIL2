def find_set(v):
    if v == parents[v]:
        return v

    parents[v] = find_set(parents[v])
    return parents[v]

def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 사이클 제
    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())    # V+1:노드 수, E:간선
    graph = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph.append((n1, n2, w))

    graph.sort(key=lambda x:x[2])       # 가중치 기준 sort

    parents = [i for i in range(V+1)]
    cnt, total_weight = 0, 0
    for s, e, weight in graph:
        if find_set(s) != find_set(e):
            union(s, e)
            cnt += 1
            total_weight += weight

            if cnt == V:
                break
    print(f'#{tc} {total_weight}')