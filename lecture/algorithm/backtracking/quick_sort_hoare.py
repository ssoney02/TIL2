#left, right: 작업 범위
def partitioning(left, right):
    pivot = arr[left]

    i = left + 1
    j = right

    while i <= j:
        # i = 큰 값을 검색하면서 오른쪽으로 진행
        while i <= j and arr[i] <= pivot:
            i += 1
        # j = 작은 값을 검색하면서 왼쪽으로 진행
        while i <= j and arr[j] >= pivot:
            j -= 1

        # SWAP
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # pivot 위치를 확정시켜주기 (j와 바꾸기)
    arr[left], arr[j] = arr[j], arr[left]
    return j

def quick_sort(left, right):
    if left < right:
        # pivot 기준으로 정렬
        pivot = partitioning(left, right)
        # 왼쪽 진행
        quick_sort(left, pivot-1)
        # 오른쪽 진행
        quick_sort(pivot+1, right)


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(0, len(arr) - 1)
print(arr)