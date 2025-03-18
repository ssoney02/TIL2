def partitioning(left, right):
    pivot = arr[left]

    i = left + 1
    j = right

    while i <= j:
        # i : 큰 값을 검색하면서 오른쪽으로 진행
        while i <= j and arr[i] <= pivot:
            i += 1
        # j : 작은 값을 검색하면서 왼쪽으로 진행
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j

# 퀵 정렬
# 작업 영역 구분, pivort 위치 확정
def quick_sort(left, right):
    if left < right:
        pivot = partitioning(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    quick_sort(0, N-1)
    print(f'#{tc} {arr[N//2]}')