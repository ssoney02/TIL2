arr = [69, 10, 30, 2, 16, 8, 31, 22]
# 병합 정렬할

def merge(left, right):
    res = [0] * (len(left) + len(right))
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res[l+r] = left[l]
            l += 1

        else:
            res[l+r] = right[r]
            r += 1

    # 한 쪽이 먼저 다 끝나버렸으면
    while l < len(left):    # l이 먼저끝났으면 알아서 넘어갈
        res[l+r] = left[l]
        l += 1
    while r < len(right):
        res[l+r] = right[r]
        r += 1

    return res

def merge_sort(li):
    if len(li) == 1:
        return li

    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]

    # 계속 분
    left_lst = merge_sort(left)
    right_lst = merge_sort(right)

    merged_lst = merge(left_lst, right_lst)
    return merged_lst

res = merge_sort(arr)
print(res)