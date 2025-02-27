T = int(input())
for tc in range(1, T+1):
    n = int(input())    # 삼각형의 크기 = 마지막 줄 수의 개수
    triangle = [[0]*(i+1) for i in range(n)]