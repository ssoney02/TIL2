T = int(input())

for tc in range(1, T+1):
    word = list(input())
    N = len(word)
    new_word = [0] * N

    for i in range(N):
        if word[N-i-1] == 'b':
            new_word[i] = 'd'
        elif word[N-i-1] == 'd':
            new_word[i] = 'b'
        elif word[N-i-1] == 'p':
            new_word[i] = 'q'
        else:
            new_word[i] = 'p'

    result = ''.join(new_word)
    print(f'#{tc} {result}')