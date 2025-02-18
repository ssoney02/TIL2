# 4:50 ~ 5:05
T = 10
for tc in range(1, T+1):
    n = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0
    for i in range(2, n-2): # 양끝 제외, 건물이 있는구간만 순회
        max_height = 0
        if buildings[i] == max(buildings[i-2:i+3]):
            #buildings[i]가 -2~2 구간에서 최대이면
            # i-2부터 i+3 구간의 buildings 중에 buildings[i]가 최대이면 확인
            # 높이가 동일한게 있으면..? 어차피 뺄거니까 상관x
            for k in [-2, -1, 1, 2]:
                # 나머지들 중에서 최대 높이 찾고, 뺌 -> 걔네만 조망권 확
                max_height = max(max_height, buildings[i+k])
            cnt += (buildings[i] - max_height)
    print(f'#{tc} {cnt}')
