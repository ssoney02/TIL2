T = int(input())

for tc in range(1, T+1):
    a, b = input().split()
    a_lst = list(a)
    b_lst = list(b)

    #n_i, n_j 안쓰고 +k로 돌리기..
    i = 0
    j = 0
    cnt = len(a) # len(a)로 시작해서 완벽 일치하는게 있으면 len(b)-1 만큼 빼주면됨
    while i < len(a):
        if a_lst[i] == b_lst[j]:    # 일치하면 다음꺼 탐색
            for k in range(1, len(b_lst)):
                if a_lst[i+k] != a_lst[j+k]:
                    i += 1
                    j = 0
                    break
            else:
                i += (len(b)-1) # 확인!!!!!