from itertools import permutations
import copy
import math

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 숫자의 개수
    counts = list(map(int, input().split()))   # 순서대로 +,-,*,/ 개수
    numbers = list(map(int, input().split()))
    # copy_numbers = copy.deepcopy(numbers)


    n_counts = []
    for i in range(len(counts)):
        for j in range(counts[i]):
            n_counts.append(i)
    # print(n_counts)

    unique_permutations = set(permutations(n_counts))  # 그냥 가능한 경우 다 구해놓고 중복 제거!
    ans = []
    for perm in unique_permutations:        # 연산자 조합 하나씩 돌면서
        # print(perm)
        top1 = -1
        top2 = 0
        copy_numbers = []
        for n in numbers:
            copy_numbers.append(n)
        # print(copy_numbers)

        while top1 <= len(copy_numbers)-3:
            top1 += 1
            op1 = copy_numbers[top1]
            top1 += 1
            op2 = copy_numbers[top1]
            if op2 == 0:
                break

            if perm[top2] == 0:
                copy_numbers[top1] = op1 + op2
            elif perm[top2] == 1:
                copy_numbers[top1] = op1 - op2
            elif perm[top2] == 2:
                copy_numbers[top1] = op1 * op2
            elif perm[top2] == 3:
                # if op1 < 0:
                #     -(-op1 // op2)
                copy_numbers[top1] = int(op1 / op2)
            top2 += 1
            top1 -= 1
        ans.append(copy_numbers[-1])


    # print(ans)
    # print(max(ans))
    # print(min(ans))
    print(f'#{tc} {max(ans)-min(ans)}')