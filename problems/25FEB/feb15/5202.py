import sys
sys.stdin = open("5202input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    time_lst = [0] * 24

    work_lst = [list(map(int, input().split())) for _ in range(n)]
    print(time_lst)
    print(work_lst)


    # time_lst에 신청서 수 담
    for w in work_lst:
        for idx in range(w[0], w[1]):
            time_lst[idx] += 1
            # time_lst에 신청서를 추가해야되는데
            # 추가할때 값이 2 이상이되는 구간이 있으면 몇갠지 cnt
            # 신청서들 구간을 다 돌면서(work_lst를 다 돌면서)
            # 2이상인게 몇갠지...
    max_apply = max(time_lst)
    # 시간대별 신청서 수를 다 넣어놓고
    # 신청 건수 max_신청 값 가져와서
    # 각 인덱스 신청서 구간 돌면서 max_신청이 몇갠지 cnt_lst에 넣어둠
    # 가장 많은 cnt_lst 값의 인덱스를 반환해서
    # 신청서 리스트에서 pop하고 time_lst에서도 pop한 신청서 구간만큼 -=1
    # max_신청 == 1이 될 때까지 반복
    while max_apply > 1:
        if max_apply in time_lst:
            cnt_lst = []
            for i in range(len(work_lst)):
                # 신청서 별로 2가 몇개 있는지 cnt해서 max인 work_lst의 인덱스를 반환해서 제
                cnt = time_lst[work_lst[i][0]:work_lst[i][1]].count(max_apply)
                #근데 각 신청서 구간에서 cnt를셀때 신청서의 시작과 끝만 2면 괜찮음...
                # count 말고 진짜 인덱스 구간 다 가져와서 하나하나 돌면서 += 1로 cnt하면 .. 가능할수도..
                # if max_apply in work_lst and max_apply not in time_lst[work_lst[1]]:time_lst[work_lst[-1] 면.. 괜춘.. 에바..
                cnt_lst.append(cnt)
            # 근데.. 2가 하나만 겹치면 ㄱㅊ음.....................(끝나자마자 시작하기는 가능..)
            idx = cnt_lst.index(max(cnt_lst))
            pop_apply = work_lst[idx]
            print(pop_apply)

        work_lst.pop(idx)
        print(f'new_work_lst: {work_lst}')
        for k in range(pop_apply[0], pop_apply[1]):
            time_lst[k] -= 1
        # 다 돌았으면 max_apply 갱신
        max_apply = max(time_lst)
        if max_apply == 1:
            break
        print(f'new_max_apply: {max_apply}')
    print(work_lst)

    print(cnt_lst)
    print(f'#{tc} {len(work_lst)}')

    print(time_lst)