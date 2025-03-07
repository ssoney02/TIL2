# M의 우측 N개를 확인할 예정
def solution():
    target = M
    # N번 확인한다.
    for _ in range(N):
        # 맨 우측 비트가 1인지 체크
        if target & 0x1 == 0:   # target & 1도 가능 (0x1, 0b1, 1 다 사용 가능)
            # 0x1: 다른 언어랑 같이 사용할 때 비트연산이라는 것을 명시하기 위해 사용하는 것..
            return False
        # 맨 우측 비트를 삭제
        target = target >> 1

# 단순하게 하는 방법
def solution2():
    # N개의 1을 구함
    mask = (1 << N) - 1
    result = (M & mask) == mask
    return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = solution()