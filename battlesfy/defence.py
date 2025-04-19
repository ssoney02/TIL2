import socket
from collections import deque

# --- 네트워크 관련 함수 ---
HOST = '127.0.0.1'
PORT = 8747
sock = socket.socket()

def init(nickname) -> str:
    try:
        print(f"[STATUS] Trying to connect to {HOST}:{PORT}")
        sock.connect((HOST, PORT))
        print("[STATUS] Connected")
        init_command = f"INIT {nickname}"
        return submit(init_command)
    except Exception as e:
        print("[ERROR] Failed to connect. Please check if Battle SSAFY is waiting for connection.")
        print(e)
        return None

def submit(string_to_send) -> str:
    try:
        sock.send((string_to_send + " ").encode("utf-8"))
        return receive()
    except Exception as e:
        print("[ERROR] Failed to send command.")
        print(e)
        return None

def receive() -> str:
    try:
        data = sock.recv(1024)
        game_data = data.decode()
        if game_data and int(game_data[0]) > 0:
            return game_data
        close()
        return None
    except Exception as e:
        print("[ERROR] Failed to receive data.")
        print(e)
        return None

def close():
    try:
        if sock is not None:
            sock.close()
        print("[STATUS] Connection closed")
    except Exception as e:
        print("[ERROR] Connection close error.")
        print(e)

# --- 데이터 파싱 ---
map_data = []    # 2차원 맵 정보: map_data[row][col]
allies = {}      # 아군 정보: 예) allies["A"] = [체력, 방향, 보유 일반 포탄, 보유 대전차 포탄]
enemies = {}     # 적군 정보: 예) enemies["X"] = [체력]
codes = []       # 암호문 리스트

def parse_data(game_data_str):
    global map_data, allies, enemies, codes
    rows = game_data_str.split("\n")
    row_index = 0
    header = rows[row_index].split(" ")
    map_height = int(header[0])
    map_width = int(header[1])
    num_allies = int(header[2])
    num_enemies = int(header[3])
    num_codes = int(header[4])
    row_index += 1

    # 맵 정보 파싱
    map_data = []
    for i in range(map_height):
        map_data.append(rows[row_index + i].split(" "))
    row_index += map_height

    # 아군 정보 파싱
    allies = {}
    for i in range(num_allies):
        parts = rows[row_index + i].split(" ")
        ally_name = parts[0]
        allies[ally_name] = parts[1:]
    row_index += num_allies

    # 적군 정보 파싱
    enemies = {}
    for i in range(num_enemies):
        parts = rows[row_index + i].split(" ")
        enemy_name = parts[0]
        enemies[enemy_name] = parts[1:]
    row_index += num_enemies

    # 암호문 파싱
    codes = []
    for i in range(num_codes):
        codes.append(rows[row_index + i])

# --- 이동/경로 탐색 관련 보조 함수 ---

def find_position(target, mat):
    """맵(mat)에서 target 기호의 [row, col] 위치를 반환"""
    for i, row in enumerate(mat):
        for j, cell in enumerate(row):
            if cell == target:
                return [i, j]
    return None

def is_passable(cell):
    """
    기존 is_passable()은 잔디("G")나 내 전차("A")만 허용.
    여기서는 목적지인 적 포탑("X")도 허용하고,
    "E"로 시작하는 다른 전차는 장애물로 간주한다.
    """
    return cell in ["G", "A", "X"]

def move_towards(current, target):
    """
    현재 위치 current에서 target까지 한 칸 이동하는 명령 반환.
    (예: 'U A', 'D A', 'L A', 'R A'; 이미 도착 시 'S')
    """
    cur_r, cur_c = current
    tar_r, tar_c = target
    if cur_r < tar_r:
        return "D A"
    elif cur_r > tar_r:
        return "U A"
    elif cur_c < tar_c:
        return "R A"
    elif cur_c > tar_c:
        return "L A"
    return "S"  # 이미 도착했으면

def bfs(start, target):
    """
    start부터 target까지의 최단 경로를 BFS로 찾는다.
    장애물: 'W', 'R', 'T', 'F' 및 'E'로 시작하는 전차(단, 시작/목적지 제외)
    경로가 없으면 None 반환.
    """
    height = len(map_data)
    width = len(map_data[0])
    visited = [[False] * width for _ in range(height)]
    route = [[None] * width for _ in range(height)]
    si, sj = start
    q = deque([(si, sj)])
    visited[si][sj] = True

    while q:
        i, j = q.popleft()
        if (i, j) == tuple(target):
            break
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < height and 0 <= nj < width:
                # 목표가 아닌 경우에는 "E" 전차를 장애물로 간주
                if not visited[ni][nj] and (map_data[ni][nj] in ["G", "A", "X"]):
                    visited[ni][nj] = True
                    route[ni][nj] = (i, j)
                    q.append((ni, nj))
    if route[target[0]][target[1]] is None:
        return None
    path = []
    cur = target
    while cur != start:
        path.append(cur)
        cur = route[cur[0]][cur[1]]
    path.append(start)
    path.reverse()
    return path

# --- 적 전차 탐지 및 사격 ---
def enemy_within_range(my_pos, distance=3):
    """
    내 위치 my_pos에서 상, 하, 좌, 우 직선 거리 distance(기본 3) 이내에
    'E'로 시작하는 적 전차가 있으면 그 위치를 반환합니다.
    """
    r, c = my_pos
    height = len(map_data)
    width = len(map_data[0])

    # 위쪽 확인
    for i in range(1, distance + 1):
        if r - i >= 0 and map_data[r - i][c].startswith("E"):
            return (r - i, c)
    # 아래쪽 확인
    for i in range(1, distance + 1):
        if r + i < height and map_data[r + i][c].startswith("E"):
            return (r + i, c)
    # 왼쪽 확인
    for i in range(1, distance + 1):
        if c - i >= 0 and map_data[r][c - i].startswith("E"):
            return (r, c - i)
    # 오른쪽 확인
    for i in range(1, distance + 1):
        if c + i < width and map_data[r][c + i].startswith("E"):
            return (r, c + i)

    return None

def get_attack_direction(my_pos, enemy_pos):
    """
    내 탱크와 적 전차의 상대 위치를 비교하여 공격할 방향('U', 'D', 'L', 'R') 결정.
    """
    r, c = my_pos
    er, ec = enemy_pos
    if abs(er - r) >= abs(ec - c):
        return "U" if er < r else "D"
    else:
        return "L" if ec < c else "R"

# --- Fallback 이동 명령 (경로 탐색 실패 시) ---
flag_actions = ["U A", "D A", "R A", "L A"]
flag_index = 0

# --- (예시) 명령 생성 함수 ---
# 원래 코드에서 generate_command() 함수가 호출되므로, 여기서는 간단히
# 경로의 다음 칸으로 이동하는 move_towards()를 사용하는 예시를 추가합니다.
def generate_command(path, mega_ammo):
    # path[0]: 현재 위치, path[1]: 다음 이동 셀
    current = path[0]
    next_pos = path[1]
    return move_towards(current, next_pos)

# --- 메인 게임 루프 ---
NICKNAME = "오세훈(서울시장)"
game_data = init(NICKNAME)

while game_data is not None:
    print(f"----입력데이터----\n{game_data}\n----------------")
    parse_data(game_data)

    # (테스트용) 맵, 아군, 적군, 암호문 정보 출력
    height = len(map_data)
    width = len(map_data[0])
    print(f"\n[맵 정보] ({height} x {width})")
    for row in map_data:
        print(" ".join(row))
    print(f"\n[아군 정보] (총 {len(allies)}명)")
    for k, v in allies.items():
        if k == "A":
            print(f"A (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 메가 포탄: {v[3]}개")
        elif k == "H":
            print(f"H (아군 포탑) - 체력: {v[0]}")
        else:
            print(f"{k} (아군 탱크) - 체력: {v[0]}")
    print(f"\n[적군 정보] (총 {len(enemies)}마리)")
    for k, v in enemies.items():
        if k == "X":
            print(f"X (적 포탑) - 체력: {v[0]}")
        else:
            print(f"{k} (적 탱크) - 체력: {v[0]}")
    print(f"\n[암호문 정보] (총 {len(codes)}개)")
    for code in codes:
        print(code)

    # 현재 내 탱크('A')와 아군 포탑('H') 위치 검색
    my_pos = find_position("A", map_data)
    turret_pos = find_position("H", map_data)
    if my_pos is None or turret_pos is None:
        print("[ERROR] 내 탱크 또는 아군 포탑의 위치를 찾지 못했습니다.")
        game_data = submit("A")
        continue

    # 우선, 내 탱크 주변 맨해튼 거리 3 이내에 적 전차('E')가 있는지 확인하여 있다면 사격
    enemy_pos = enemy_within_range(my_pos, 3)
    if enemy_pos is not None:
        attack_dir = get_attack_direction(my_pos, enemy_pos)
        command = attack_dir + " F S"
        print(f"[ACTION] 적 전차 감지 (내 위치로부터 3 이내): {enemy_pos} → 사격 명령: {command}")
        game_data = submit(command)
        continue

    # 이동 목표 결정
    # 만약 아군 포탑의 위치가 왼쪽 제일 아래 ([height-1, 0])라면,
    # 내 탱크는 포탑 기준으로 [i-3, j+3] 위치로 이동하여 방어
    # 만약 아군 포탑의 위치가 오른쪽 제일 위 ([0, width-1])라면,
    # 내 탱크는 포탑 기준으로 [i+3, j-3] 위치로 이동하여 방어
    if turret_pos == [height - 1, 0]:
        target = [turret_pos[0] - 3, turret_pos[1] + 3]
        print(f"[INFO] 포탑이 왼쪽 제일 아래에 있으므로 방어 위치 목표: {target}")
    elif turret_pos == [0, width - 1]:
        target = [turret_pos[0] + 3, turret_pos[1] - 3]
        print(f"[INFO] 포탑이 오른쪽 제일 위에 있으므로 방어 위치 목표: {target}")
    else:
        target = find_position("X", map_data)
        if target is None:
            print("[ERROR] 적 포탑의 위치를 찾지 못했습니다.")
            game_data = submit("A")
            continue

    # BFS로 최단 경로 탐색 (목표: target)
    path = bfs(tuple(my_pos), tuple(target))
    if path is None:
        print("[WARNING] 목표로 가는 경로를 찾지 못했습니다. fallback 행동 실행.")
        command = flag_actions[flag_index]
        flag_index = (flag_index + 1) % len(flag_actions)
    else:
        try:
            mega_ammo = int(allies["A"][3])
        except (KeyError, ValueError):
            mega_ammo = 0
        command = generate_command(path, mega_ammo)
        print(f"[ACTION] 경로 탐색 결과 → 명령: {command}")

    print(f"[COMMAND] {command}")
    game_data = submit(command)

close()
