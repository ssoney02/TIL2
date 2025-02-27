# def perm(cnt):

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 숫자의 개수
    counts = list(map(int, input().split()))   # 순서대로 +,-,*,/ 개수
    numbers = list(map(int, input().split()))
    top1 = -1
    top2 = 0
    while top1 <= len(numbers):
        top1 += 1
        op1 = numbers[top1]
        top1 += 1
        op2 = numbers[top1]
        # while top2 <= len(counts):
        # top 확인은 한 번만 해야
            if counts[top2] != 0:됨
                counts[top2] -= 1
            else:
                top2 += 1
