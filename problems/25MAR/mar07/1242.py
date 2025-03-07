# 배열 -> 2진수로 변환
# 검증코드 체크
binary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
          '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

# import sys
# sys.stdin = open("1242input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    codes = [input() for _ in range(N)]
    print(codes)
    max_len = -float('inf')

    for code in codes:
        if len(set(code)) > 1:    # code에 0이 아닌 것이 하나라도 있으면 실행
            if len(set(code)) > max_len:    # 요소가 가장 많은거 대상으로만 실행(일부만 들어있는 행도있음)
                max_len = max(max_len, len(set(code)))
                n_code = list(code)
                # print(n_code)
                for i in range(M):
                    if n_code[i] in binary.keys():
                        n_code[i] = binary[n_code[i]]
    print(n_code)

    n_code = ''.join(n_code)
    print(n_code)
    cnt = []
    idx = 0     # 초기 idx = 0
    for i in range(1, len(n_code)):
        if n_code[i-1] != n_code[i]:
            cnt.append(i-idx)   # (이번 인덱스 - 직전 인덱스) 저장
            idx = i             # 직전 idx 저장, 갱신
    print(cnt)
    print(len(cnt))

    # 만약 코드가 여러개면 중간에 공백 존재 가능 (이상치.. 제거..) 이상치 기준????????
    # 두께가 1이 아니면 공백 제외 값들 중.. 4보다 큰게 있을 것 => 두께 배수만큼 나눠주기
    if min(cnt) > 1:
        # min(cnt) == 1 이어야됨..
        for j in range(len(n_code)//4):
            pass

