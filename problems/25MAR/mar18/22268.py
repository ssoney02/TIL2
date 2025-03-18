def merge(left, right):
    global cnt
    result = [0] * (len(left) + len(right))
    l = r = 0
    if left[-1] > right[-1]:
        cnt += 1
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1

    while l < len(left):
        result[l+r] = left[l]
        l += 1
    while r < len(right):
        result[l+r] = right[r]
        r += 1

    return result

def merge_sort(li):
    if len(li) == 1:
        return li

    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    merged_list = merge(left_list, right_list)
    return merged_list

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr[N // 2 - 1])
    cnt = 0
    merged_arr = merge_sort(arr)
    # print(merged_arr)

    print(f'#{tc} {merged_arr[N//2]} {cnt}')

