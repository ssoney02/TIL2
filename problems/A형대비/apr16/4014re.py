#4014 활주로 건설
T = int(input())
def check_row(ground):
    global cnt

    for i in range(N):
        # 만약 지형 높이가 다 동일하다면 그냥 cnt+=1 하고 다음 줄 확인
        if ground[i].count(ground[i][0]) == N:
            cnt += 1
            continue
        else:
            # 정방향 순회 (내려가는 경우만 확인)
            for j in range(N-1):
                if ground[i][j] - ground[i][j+1] > 1:       # 1보다 크면 그냥 건설 못함 -> 다음 i 확인
                    break  # for j
                elif ground[i][j] - ground[i][j+1] == 1:    # 1만큼 낮아지면
                    if N - j < X: break
                    # j+1, j+2 ,, j+X의 높이가 j+1의 높이와 동일해야됨
                    if any(ground[i][k] != ground[i][j+1] for k in range(j+2, j+X+1)):
                        # 뭐하나라도 다른게 있다면
                        break   # for j
            # 역방향 순회 (내려가는 경우만 확인)
            for r_j in range(N-1, 0, -1):
                if ground[i][r_j] - ground[i][r_j-1] > 1:
                    break
                elif ground[i][r_j] - ground[i][r_j-1] == 1:
                    if r_j < X: break
                    if any(ground[i][k] != ground[i][r_j-1] for k in range(r_j-2, r_j-X-1, -1)):
                        break
            else:
                cnt += 1
    return cnt
for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    cnt1 = check_row(arr)
    rotated_arr = list(map(list, zip(*arr)))
    res = check_row(rotated_arr)
    print(f'#{tc} {res}')