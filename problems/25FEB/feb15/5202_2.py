import sys
sys.stdin = open("5202input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    work_lst = [list(map(int, input().split())) for _ in range(n)]
    # print(work_lst)
    # 시작 시간 기준 정
    work_lst.sort() # .sort()는 반환값 x 원래 리스트를 sort 하는 것..

    # print(f'sorted work list : {work_lst}')
    #sorted_work_lst를 뒤에서부터 돌면서 만약 work_lst[idx-1][1]=<work_lst[idx][0]이면 cnt_lst추가, 아니면 다음 idx 순
    cnt_lst = [work_lst[-1]] # 뒷쪽부터 시작하니까 제일 마지막 신청서는 추가하고 시
    # 비교하는 신청서 idx랑 현재 idx랑 따로 지정해서 돌려야할듯...?
    # 아니면 cnt_list에 추가하고, 그 값의 인덱스를 work_lst에서 찾아서 반환 시키든가..
    idx = n-1
    while idx >= 0:
        n_idx = work_lst.index(cnt_lst[-1])
        if work_lst[idx-1][1] <= work_lst[n_idx][0]:
            cnt_lst.append(work_lst[idx-1])
        idx -= 1

    print(f'#{tc} {len(cnt_lst)}')



    # 끝나는 시간 기준으로 정렬해놓고
    # 현재 작업의 끝나는 시간 다음 시작시간이 현재 끝나는시간에 가장 가까운 것
    # 그러면 그냥 뒤에서부터 시작시간 기준으로 역순 정렬해놓고, 끝나는시간이 가장 가까운거 해도 되는거아닌가..?
