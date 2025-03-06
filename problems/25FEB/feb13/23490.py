#250213 2:30 ~ 2:40 포기..

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(arr)
    # 0부터 24까지 시간 배열 만들어 놓고
    # 가능한거 다 넣어둠 ( 신청 시간 에 + 1씩)
    # 겹치는게 2하나면 ㄱㅊ
    # 3이상이거나, 2가 2개 이상이면 신청건 별로 겹치는 수 세서 max인걸 제외?

    time_lst = [0] * 25     # 0시부터 24시까지
    for i in range(n):
        for j in range(arr[i][0], arr[i][1]+1):
            time_lst[j] += 1

    # 겹치는게
    print(time_lst)





