T = 10
for tc in range(1, T+1):
    n, nums = input().split()
    # print(n)
    # print(nums)
    stack = [10] * 100 # 0으로 채워두면.. 첫 숫자가 0일때 일치한다고 판단해버릴 수 있을 듯..
    top = -1

    for i in range(len(nums)):
        if stack[top] != nums[i]:
            top += 1
            stack[top] = nums[i]
        elif stack[top] == nums[i]:
            top -= 1

    result = stack[:top+1]
    ans = ''.join(result)
    print(f'#{tc} {ans}')
