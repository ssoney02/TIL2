import sys
sys.stdin = open("1959input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 무조건 b가 a보다 길다 생각하고 코드 짜기
    sum_lst = []

    if len(a) > len(b):
        a, b = b, a
    # 밀 때: a[i+k] = a[i]
    # 밀때마다 a 리스트 자체가 갱신되니까.. 그냥 while문 돌려서 길이같아지면 break하는게
    while len(a) <= len(b):
        total = 0
        for i in range(len(a)):
            total += a[i]*b[i] # 곱해서 더함
        # total값을 sum_lst에 추가
        sum_lst.append(total)
        # 1회차.. 곱하고 값 total_lst에 추가했으면
        # 한번 밀어야됨
        a.insert(0,0) #a[0]에 0 삽
    print(f'#{tc} {max(sum_lst)}')



