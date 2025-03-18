def find_set(total, idx):
    if total == 10: # 합이 10이면 return
        print(numset)
        return

    for i in range(idx, N):
        total += powerset[i]
        numset.append(powerset[i])
        # n_set = numset + [powerset[i]]
        find_set(total, i + 1)
        total -= powerset[i]
        numset.pop()
        # numset = n_set - [powerset[i]]

powerset = [1,2,3,4,5,6,7,8,9,10]
N = len(powerset)
numset = []
find_set(0, 0)