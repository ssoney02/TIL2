T = int(input())

for tc in range(1, T+1):
    word = list(input())
    n = len(word)
    new_word_list = []
    for i in range(n-1, -1, -1):
        new_word_list.append(word[i])
    original_word = ''.join(word)
    new_word = ''.join(new_word_list)

    if original_word == new_word:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')
