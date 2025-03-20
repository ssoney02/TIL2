def find_set(x):  # 대표자 검색
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
    N, E = map(int, input().split())
    edges = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append((s, e, w))

    edges.sort(key=lambda x: x[2])  # 구간 길이 기준으로 오름차순
    parents = [i for i in range(N+1)]  # 정점 기준으로 make_set

    cnt = 0
    result = 0  # 거리
    # print('e', edges)

    for u, v, d in edges:

        if find_set(u) != find_set(v):
            # print(u, v, d)
            union(u, v)
            cnt += 1
            result += d

            if cnt == N:
                break

    print(f'#{tc} {result}')
