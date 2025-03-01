def find_target(n_idx, res):
    global target, ans
    # numbers 리스트 다 돌면 중단
    if n_idx == len(numbers):
        # 최종 연산 결과가 target이랑 일치하면 ans + 1
        if res == target:
            ans += 1
        return

    # 정수를 그대로 사용하는 경우
    tmp_res = res
    tmp_res += numbers[n_idx]
    find_target(n_idx+1, tmp_res)

    # -를 붙이는 경우
    tmp_res = res
    tmp_res -= numbers[n_idx]
    find_target(n_idx+1, tmp_res)

numbers = list(map(int, input().split()))
target = int(input())
ans = 0

init_idx = 0
init_res = 0

find_target(init_idx, init_res)

print(ans)