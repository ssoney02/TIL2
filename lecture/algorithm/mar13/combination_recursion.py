arr = ['A', 'B', 'C', 'D', 'E']
n = 3

path = []

# 5명 중 3명을 뽑는 문제
def recur(cnt, idx):
    if cnt == n:    # n명 다 뽑으면 return
        print(*path)
        return

    # 5명을 고려해야 함
    for i in range(idx, len(arr)):
        path.append(arr[i])
        recur(cnt + 1, i + 1)
        path.pop()


recur(0)

# for target in range(1 << 5):
#     print(target)