T = int(input())
for tc in range(1, T+1):
    n = int(input()) # 버스 노선 수

    bus_route = [list(map(int, input().split())) for _ in range(n)] # 노선의 시작점, 끝점 정보를 담은 리스트
    # print(bus_route)

    p = int(input())
    c = [int(input())  for _ in range(p)] # 개수 세야하는 버스 정류장 번호 주어준 것
    # print(c)
    bus_stop = [0] * 5000 # 버스 정류장 만들어둠
    for i in range(n):
        for k in range(bus_route[i][0]-1, bus_route[i][1]): # 끝 범위는 -1 + 1 인덱스 까지
        # 버스 노선 시작점 버스 정류장 번호 -> 인덱스는 번호-1
        # 버스 노선 끝점 버스 정류장 번호 -> 인덱스는 번호 -1
            bus_stop[k] += 1
    result = []
    for j in range(p):
        result.append(str(bus_stop[c[j]-1]))
    s_result = ' '.join(result)
    print(f'#{tc} {s_result}')
