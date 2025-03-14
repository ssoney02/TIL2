import sys
sys.stdin = open('16811input.txt', 'r')

def check_idx(line, cnt):
    global box1, box2, box3, line1
    if cnt == 2:    # 두번 구분 지어주면 함수 종료
        return
    while line <= N-1:
        for i in range(line, N):
            if carrots[i] == carrots[i+1]:      # 나랑 다음값이 같으면
                line += 1
            else:       # 나랑 다른 값이 나오면 line까지 끊어서 박스 하나 만들어줌
                if cnt == 0:    # 첫번째로 구분짓는 거면
                    for c in carrots[:line+1]:
                        box1.append(c)

                    print(box1)
                    line1 = line
                    cnt += 1
                    check_idx(line, cnt)
                    box1 = []
                    cnt -= 1
                else:           # 두번째로 구분짓는 거면
                    box2 = carrots[line1:line]
                    box3 = carrots[line:]
                    print(box2)
                    print(box3)
                    check_idx(line, cnt)
                    box2, box3 = [], []
                    cnt -= 1



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()
    print(carrots)
    # 박스1에 idx1당근 까지 넣을 것 , 박스2에 idx2 당근 까지 넣을 것
    # box1 = carrots[:idx1+1]
    # box2 = carrots[idx1:idx2+1]
    check_idx(0, 0)
    line1 = 0
    box1, box2, box3 = [], [], []