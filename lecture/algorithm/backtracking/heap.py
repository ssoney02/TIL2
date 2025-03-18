import heapq
# heappush, heappop, heapify
arr = [20, 15, 19, 4, 13, 11]

# 1. 기본 리스트를 heap으로 만들기
heapq.heapify(arr)
print(arr)

# 2. 하나씩 데이터를 추가
