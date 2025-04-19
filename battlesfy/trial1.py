from collections import deque


def bfs_shortest_path(grid, start, target):
    rows = len(grid)
    if rows == 0:
        return None
    cols = len(grid[0])

    start_row, start_col = start
    target_row, target_col = target

    # 시작/목적 좌표가 유효한지 (장애물이 아닌지) 확인
    if grid[start_row][start_col] != 0 or grid[target_row][target_col] != 0:
        print("시작 또는 목적 좌표가 이동 불가능한 지점입니다.")
        return None

    # 방문 여부 기록 (2차원 리스트)
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    # 각 좌표의 이전 좌표를 저장 (None: 아직 기록 없음)
    prev = [[None for _ in range(cols)] for _ in range(rows)]

    queue = deque()
    queue.append(start)
    visited[start_row][start_col] = True

    # 상하좌우 이동 (필요에 따라 대각선 등 다른 이동도 추가 가능)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # BFS 탐색
    while queue:
        current = queue.popleft()
        cur_row, cur_col = current

        # 목적지에 도달한 경우 종료
        if current == target:
            break

        # 인접한 좌표들 확인
        for dr, dc in directions:
            new_row = cur_row + dr
            new_col = cur_col + dc
            # 범위 내에 있고, 방문하지 않았으며, 이동 가능한 셀(0)인 경우
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if not visited[new_row][new_col] and grid[new_row][new_col] == 0:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))
                    # 현재 좌표가 인접 좌표의 이전 노드로 기록됨
                    prev[new_row][new_col] = (cur_row, cur_col)

    # 목적지까지의 경로가 존재하는지 확인
    if not visited[target_row][target_col]:
        print("목적지까지의 경로가 존재하지 않습니다.")
        return None

    # 경로 재구성: 목적지부터 시작점까지 역으로 추적
    path = []
    current = target
    while current is not None:
        path.append(current)
        cur_r, cur_c = current
        current = prev[cur_r][cur_c]

    # 역추적한 경로를 뒤집으면 시작부터 목적까지의 경로가 됨
    path.reverse()
    return path


# 예시 2차원 격자 (0: 이동 가능, 1: 장애물)
grid = [
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)  # 시작 좌표
target = (3, 3)  # 목적 좌표

shortest_path = bfs_shortest_path(grid, start, target)
print("최단 경로:", shortest_path)
