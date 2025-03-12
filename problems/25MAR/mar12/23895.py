from itertools import permutations


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    battery_use = [list(map(int, input().split())) for _ in range(N)]
    # idx: 사무실,관리구역 번호 - 1
    # [0]: 사무실 [1]~[N-1]: 관리구역
    # battery_use[출발구역번호-1][도착구역번호-1]

    # 각 구역은 한 번씩만 방문
    # 1~N-1 순열(순서고려 o)
    area = [i for i in range(1, N)]

    perms = []
    # for perm in permutations(area, N-1):
    #     perms.append(perm)

    # battery[0][com[0]] + battery[com[0]][com[1]] + battery[com[i]][com[i+1]] + ..[com[N-1]][0]
    min_battery = float('inf')
    for p in permutations(area, N-1):
        battery = 0
        # 0에서 출발하는 것 계산
        battery += battery_use[0][p[0]]
        # 구역 내에서 도는 것 계산
        for j in range(N-2):
            battery += battery_use[p[j]][p[j+1]]
        # 다 돌고 사무실로 돌아가는 것 계산
        battery += battery_use[p[N-2]][0]
        min_battery = min(min_battery, battery)
    print(f'#{tc} {min_battery}')