T = int(input())

for tc in range(1, T+1):
    word_list = [list(input()) for _ in range(5)]
    # print(word_list)
    n = 0
    n = len(word_list)
    max_len = 0
    min_len = float('inf')
    for k in range(5):
        max_len = max(len(word_list[k]), max_len)
        min_len = min(len(word_list[k]), min_len)
    result = ''
    for j in range(max_len):
        for i in range(n):
            if len(word_list[i]) < max_len and j >= len(word_list[i]):
                continue
            else:
                # print(word_list[i][j])
                result += word_list[i][j]

    print(f'#{tc} {result}')