import sys
sys.stdin = open("1240input.txt", "r")
pass_dic = {0: [2, 1, 1],
            1: [2, 2, 1],
            2: [1, 2, 2],
            3: [4, 1, 1],
            4: [1, 3, 2],
            5: [2, 3, 1],
            6: [1, 1, 4],
            7: [3, 1, 2],
            8: [2, 1, 3],
            9: [1, 1, 2]}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    passcords = [input() for _ in range(N)]
    cnt = [0]
    total_cnt = []
    ans = []
    # print(passcords)
    # print(len(passcords[1]))
    for passcord in passcords:
        if '1' in passcord:
            s_idx = passcord.index('1')     # 첫번째로 1이 나오는 인덱스 확인
        for i in range(1, M):
            if i == M-1:
                cnt.append(M)
            else:
                if passcord[i-1] != passcord[i]:
                    o_idx = i
                # 바뀌는 지점의 인덱스 값 넣어주면됨
                    cnt.append(i)

    # print(cnt)
    for c in cnt:
        if c != 0 and c != M:
            c_idx = cnt.index(c)
            # 암호 하나 당 바뀌는 구간 총 32
            n_cnt = cnt[c_idx:c_idx+32]
            break
    # print(n_cnt)
    for i in range(31, 0, -1):
        n_cnt[i] -= n_cnt[i-1]
    # print(len(n_cnt))
    # print(n_cnt)
    # 네 개씩 끊어서 나누고, 첫번째 수 제외 3개값만 비교해도 될 듯
    cords = []
    for j in range(8):
        cords.append(n_cnt[4*j + 1: 4*j + 4])
    # print(cords)
    for c in cords:
        if c in pass_dic.values():
            for key, value in pass_dic.items():
                if value == c:
                    ans.append(key)
            # matching_keys = [key for key, value in pass_dic.items() if value == c]
            # ans.append(matching_keys)

    # print(ans)
    res = 0
    result = 0
    for k in range(8):
        if k % 2 == 0:  # 자릿수: 인덱스 + 1
            res += (ans[k]*3)
        else:
            res += ans[k]
    # print(res)
    if res % 10 == 0:
        result = sum(ans)

    print(f'#{tc} {result}')