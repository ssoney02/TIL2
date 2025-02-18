T = int(input())

for tc in range(1, T+1):
    a, b = input().split()
    print(a)
    print(b)
    cnt = 0
    a_lst = list(a)
    b_lst = list(b)
    i = 0
    while i < len(b):
        for j in range(len(a)):
            if a_lst[j] == b_lst[i]:
                i += 1






