print(7 & 5)
print(7 | 5)
print(bin(7 & 5))   # 결과 자체가 이진수 형태로 출력됨

# 1. 이진수로 변환
# 2. 각 자리를 AND, OR 연산

print(bin(0x4A3 | 25))

secret_code = 1004
print(7070 ^ secret_code)
print(6258 ^ secret_code)


# shift 연산자
print(1 << 1)   # 10
print(1 << 2)   # 100
print(1 << 3)   # 1000
print(1 << 4)   # 10000

print(7 >> 1)   # 7:0b111 >> 1 오른쪽으로 한 칸 밀어내면 비트가 갈 데가 없어서 삭제됨 => 0b11 = 3(10)

num = 1
for _ in range(5):
    print(num, bin(num))
    num = num << 1


# bit 연산 응용
# 1. 부분집합의 수를 바로 구할 수 있다.
arr = [1, 2, 3, 4]  # 부분집합의 수: 16개
# 부분집합의 수: 선택하거나 안하거나 (0 or 1)의 총 경우의 수
print(f'부분 집합의 수: {1 << len(arr)}')


for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        # (1 << idx): ob1, ob10, ob100, ob1000
        # i의 idx번째 bit가 1인지 확인(=부분집합에 포함되어있는지 확인)
        if i & (1 << idx):
            print(arr[idx], end=' ')
    print()


#  <응용> 합이 10인 부분 집합만 출력해라
arr = [1, 2, 3, 4, 5, 6]
for i in range(1 << len(arr)):
    subset = []
    total = 0
    for idx in range(len(arr)):
        if i & (1 << idx):
            subset.append(arr[idx])
            total += arr[idx]
        if total == 10:
            print(f'부분집합: {subset}')

# 음수 표현
print(bin(5))
print(bin(-5))

print(~4, bin(~4))  # -5
print(~(-4))        # 3
