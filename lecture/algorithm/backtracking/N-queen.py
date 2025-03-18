# 4*4 N-Queen 문제
# (y,x) 좌표에 queen을 놓은 적이 있다
# visited 기록 방법
# 1. 이차원 배열
# 2. 일차원 배열로 효율적으로 하는 방법

# level: N개의 행에 모두 놓았다면, 성공
# branch: N개의 열
def check(row, col):
    # 1. 같은 열에 놓은 적이 있는 가
    for i in range(row):
        if visited[i][col]:
            return False
    # 2. 왼쪽 대각선(\)
    i, j = row-1, col -1
    while i >= 0 and j >= 0:
        i -= 1
        j -= 1

    # 3. 오른쪽 대각선(/)


def dfs():
    answer += 1
    return
    # 후보군: N개의 열
    for col in range(N):
        if check(row, col) is False:#기존에 같은 열이나 대각선에 놓았다면 안됨!
            continue

        visited[row][col] = 1

N = 4
visited = [[0] * N for _ in range(N)]
answer = 0      # 가능한 정답 수

dfs(0)
print(answer)