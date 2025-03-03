# import sys
# sys.stdin = open("4012input.txt", "r")
def food(cnt, tmp_i):     # nCr 조합구하는 함수
    b_lst = []
    # 종료 조건: n을 다 돌았을 때??
    # 조합의 경우를 담을 바구니
    global N, r, min_syn, f_init_syn
    if cnt == r:
        # print(f'case:{case}')
           # 초기
        for n in range(N):
            if n not in case:
                b_lst.append(n)
        # print(f'b_lst:{b_lst}')
        syn_case = []
        f_init_syn = 0
        syn(0, 0, init_syn, case)
        init_syn_a = f_init_syn
        f_init_syn = 0
        # print(f'a:{init_syn_a}')
        syn(0, 0, init_syn, b_lst)
        init_syn_b = f_init_syn
        # print(f'b:{init_syn_b}')
        min_syn = min(min_syn, abs(init_syn_a-init_syn_b))
        return

    for i in range(tmp_i, N):
        case.append(i)
        food(cnt+1, i+1)
        case.pop()
# 시너지 계산 함수
# case 별로 2개씩 시너지 생기는 조합 구해서
# 다 더
def syn(s_cnt, s_tmp_i, init_syn, c):
    global f_init_syn
    if s_cnt == 2:
        # 조합 하나가 완성되면
        init_syn += synergy[syn_case[0]][syn_case[1]]
        init_syn += synergy[syn_case[1]][syn_case[0]]
        f_init_syn += init_syn
        # print(f'f_init_syn:{f_init_syn}')
        return
    for i in range(s_tmp_i, len(c)):
        syn_case.append(c[i])
        syn(s_cnt+1, i+1, init_syn, c)
        syn_case.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    r = N // 2
    synergy = [list(map(int, input().split())) for _ in range(N)]
    case = []
    syn_case = []
    init_syn, f_init_syn = 0, 0
    min_syn = float('inf')
    food(0, 0)
    # print(total_case)

    print(f'#{tc} {min_syn}')
    # for i in range(len(case)//2):


