def recur(cnt, start):
    if cnt == N:
        print(path)
        return
    for i in range(start, 7):
        path.append(i)
        recur(cnt+1, i)
        path.pop()


N = 3
path = []

recur(0, 1)