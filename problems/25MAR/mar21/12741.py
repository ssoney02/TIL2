T = int(input())
for tc in range(1, T+1):
    time = list(map(int, input().split()))
    time_line = [0] * 101

    for i in range(2):
        for l in range(time[2*i], time[2*i+1]):
            time_line[l] += 1
    # print(time_line)
    print(f'#{tc} {time_line.count(2)}')

