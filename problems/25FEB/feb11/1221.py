import sys
sys.stdin = open("GNS_test_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1):
#     case, n = input().split()
#     num_dict = {
#         'ZRO': 0,
#         'ONE': 1,
#         'TWO': 2,
#         'THR': 3,
#         'FOR': 4,
#         'FIV': 5,
#         'SIX': 6,
#         'SVN': 7,
#         'EGT': 8,
#         'NIN': 9
#     }
#     new_dict = {}
#     for key, val in num_dict.items():
#         new_dict[val] = key
#     num_lst = list(input().split())
#     n = int(n)
#     new_lst = [0] * n
#     # print(len(num_lst))
#     while True:
#         for i in range(n):
#             num = 0
#             if new_dict[num] in num_lst:
#                 new_lst[i] = new_dict[num]
#                 num_lst.pop(new_lst.index(new_dict[num]))
#             else:
#                 num += 1
#         if len(new_lst) == n:
#             break
#     result = ' '.join(new_lst)
#     print(f'{case} {result}')


T = int(input())
for tc in range(1, T+1):
    tc_num, tmp = input().split()
    arr = input().split()
    num_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_dict = {key: val for val, key in enumerate(num_str)}

    cnt = [0] * 10
    for key in arr:
        val = num_dict[key]
        cnt[val] += 1
    print(num_dict)
    print(cnt)
    lst = []
    for i in range(10):
        if cnt[i] != 0:
            lst += [num_str[i]] * cnt[i]
    print(f'lst: {lst}')
    print(' '.join(lst))

    trial = []
    for i in range(10):
        trial += [i] * i
    print(trial)