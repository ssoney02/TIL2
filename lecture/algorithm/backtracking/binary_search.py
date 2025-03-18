def binary_search_recur(left, right, target):
    # left, right를 작업 영역으로 검색
    # left <= right 만족하면 반복

    if left > right:
        return -1
    mid = (left + right) // 2
    # 검색하면 종료
    if target == arr[mid]:
        return mid
    # 한 번 할 때 마다 left와 right를 mid를 기준으로 이동시켜주면서 진행
    # 왼쪽을 봐야한다
    if target < arr[mid]:
        return binary_search_recur(left, mid - 1, target)
    # 오른쪽을 봐야한다
    else:
        return binary_search_recur(mid+1, right, target)

# def binary_search_while(target):
#     left = 0
#     right = len(arr) - 1
#     cnt = 0
#
#     while left <= right:        # 계속 반반반반 나눠지다가 결국엔 left==right인 시점이 올 것
#         mid = (left + right) // 2
#         cnt += 1                # 검색 횟수 추가가
#        if arr[mid] == target:
#             return mid, cnt          # mid index에서 검색 완료!
#
#         # 왼쪽에 정답이 있다면
#         if target < arr[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#
#     return -1, cnt                   # -1이 리턴되면 못찾았단 뜻..!

arr = [4, 2, 9, 7, 11, 23, 19]

# 이진 검색은 항상 정렬된 데이터에 적용해야 함!
arr.sort()
# print(f'9 - {binary_search_while(9)}')
# print(f'2 - {binary_search_while(2)}')
# print(f'20 - {binary_search_while(20)}')

print(f'9 - {binary_search_recur(0, len(arr) - 1, 9)}')
print(f'2 - {binary_search_recur(0, len(arr) - 1, 2)}')
print(f'20 - {binary_search_recur(0, len(arr) - 1, 20)}')