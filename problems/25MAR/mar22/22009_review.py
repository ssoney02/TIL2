def find_set(x):
    if x == parents[x]:
        return x        # x가 해당 집합의 대표자면 그냥 x 반환

    parents[x] = find_set(parents[x])   # 경로 압축
    return parents[x]

def union(x,y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:  # 동일한 집합에 들어있는 경우
        return          # 더 합칠 필요x

    if ref_x < ref_y:
        parents[ref_y] = ref_x  # ref_y의 집합에 ref_x를 추가
    else:
        parents[ref_x] = ref_y

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())    # 노드 수: V+1, 간선 수: E
    edges = []
    for _ in range(E):
        n1, n2, weight = map(int, input().split())
        edges.append((n1, n2, weight))

    edges.sort(key=lambda x:x[2])
    parents = [i for i in range(V+1)]  # 노드 수 만큼 대표자 만듦

    cnt, res = 0, 0

    for u, v, w in edges:
        if find_set(u) != find_set(v):
            union(u, v)     # 첫번째 n1 노드부터 합치기 시작..
            cnt += 1        # 선택한 간선의 수 카운
            res += w        # MST에 간선이 포함되면 간선의 가중치 저장

            if cnt == V:    # 노드 - 1 개 만큼 간선 선택했으면 끝난것!
                break

    print(f'#{tc} {res}')