# 3:36 ~ 4:16
import sys
sys.stdin = open("23488input.txt", "r")
T = int(input())

for tc in range(1, T+1):
    n, m = map(int,input().split())
    w_list = list(map(int, input().split())) # 컨테이너별 무게
    t_list = list(map(int, input().split())) # 트럭별 적재용량

    # 트럭하나에 컨테이너 하나
    # 무게 리스트 최대값부터 돌면서 적재가능하면 바로 적재
    # 트럭 적재용량도 내림차순 정렬해야

    w_list = sorted(w_list)
    t_list = sorted(t_list)
    # w_list 먼저 거꾸로 돌면서 t_list[j] >= w_list[i] 인지 확인
    # 맞으면 pop t_list[j]
    # while문으로 돌아서.. 트럭이 0대가 되면 break
    weight = 0

    while m > 0:
        for i in range(n-1, -1, -1):
            # m -= 1
            # 지금까지 중 최대 적재 용량보다 무게가 큰 경우
            # 그냥 못 싣는 컨테이너..
            # 다른 그 다음으로 무게 큰 컨테이너 봐야됨
            if t_list[m-1] < w_list[i]:
                continue
            # 적재용량이 무게보다 크거나 같으면 적재!
            # 적재하고 그 다음으로 적재용량 많은 트럭 순회
            if t_list[m-1] >= w_list[i]:
                weight += w_list[i]
                m -= 1
                # 트럭 없으면 컨테이너 확인 그만하고 끝내야됨
                if m == 0:
                    break
        else:
            break

    print(f'#{tc} {weight}')




