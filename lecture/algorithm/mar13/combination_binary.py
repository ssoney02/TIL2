arr = ['A', 'B', 'C']
n = len(arr)


def get_sub(tar):
    print(f'target = {tar}', end=' / ')
    for i in range(n):
        # 1도 되고, 0b1도 되고, 0x1도 되는데
        # 왜 0x1 이느냐
        # -> 비트 연산임을 명시하는 권장하는 방법이라서!!(다른 언어와의 호환을 위함..)
        if tar & 0x1:   # 각 자리의 원소가 포함되어 있나요?
            print(arr[i], end='')
        tar >>= 1       # 맨 우측 비트를 삭제한다
                        # == 다음 원소를 확인하겠다.


# 전체 부분집합을 확인해야한다.
for target in range(1 << n):
    get_sub(target)

