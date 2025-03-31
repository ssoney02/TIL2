arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]


def partitioning(left, right):
    pivot = arr[left]

    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j : # 양방향에서 점점 왔는데 아직 도착 못함. 근데 진행도 못함
            # 현재 arr[i]에는 pivot보다 큰 수가 들어있고, arr[j]에는 pivot보다 작은 수가 들어있음
            arr[i], arr[j] = arr[j], arr[i]

    # 다 돌고 나와서 j < i 가 됐으면 pivot의 위치를 j위치로 교환
    arr[left], arr[j] = arr[j], arr[left]
    return j    # arr[j]위치에 pivot 고정! 그 위치 기준으로 왼쪽 오른쪽 작업영역 나눠서 다시 partitioning


def quick_sort(left, right):
    if left < right:
        # pivot 기준 정렬
        pivot = partitioning(left, right)
        quick_sort(left, pivot-1)
        quick_sort(pivot+1, right)

quick_sort(0, len(arr)-1)
print(arr)