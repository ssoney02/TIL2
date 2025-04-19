import socket

HOST = '127.0.0.1'
PORT = 8747

# 입력 데이터 분류
char_to_int = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
map_data = [[]]  # 맵 정보. 예) map_data[0][1] - [0, 1]의 지형/지물
allies = {}  # 아군 정보. 예) allies['A'] - 플레이어 본인의 정보
enemies = {}  # 적군 정보. 예) enemies['X'] - 적 포탑의 정보
codes = []  # 주어진 암호문. 예) codes[0] - 첫 번째 암호문

sock = socket.socket()

def init(nickname) -> str:
    try:
        print(f'[STATUS] Trying to connect to {HOST}:{PORT}')
        sock.connect((HOST, PORT))
        print('[STATUS] Connected')
        init_command = f'INIT {nickname}' 

        return submit(init_command)

    except Exception as e:
        print('[ERROR] Failed to connect. Please check if Battle SSAFY is waiting for connection.')
        print(e)

def submit(string_to_send) -> str:
    try:
        sock.send((string_to_send + ' ').encode('utf-8'))

        return receive()
        
    except Exception as e:
        print('[ERROR] Failed to connect. Please check if Battle SSAFY is waiting for connection.')

    return None

def receive() -> str:
    try:
        game_data = (sock.recv(1024)).decode()

        if int(game_data[0]) > 0:
            return game_data
            
        close()
    except Exception as e:
        print('[ERROR] Failed to connect. Please check if Battle SSAFY is waiting for connection.')

def close():
    try:
        if sock is not None: sock.close()
        print('[STATUS] Connection closed')
    
    except Exception as e:
        print('[ERROR] Network connection has been corrupted.')

# 입력 데이터를 파싱하여 변수에 저장
def parse_data(game_data):
    # 입력 데이터를 행으로 나누기
    game_data_rows = game_data.split('\n')
    row_index = 0

    # 첫 번째 행 데이터 읽기
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0])  # 맵의 세로 크기
    map_width = int(header[1])  # 맵의 가로 크기
    num_of_allies = int(header[2])  # 아군의 수
    num_of_enemies = int(header[3])  # 적군의 수
    num_of_codes = int(header[4])  # 암호문의 수
    row_index += 1

    # 기존의 맵 정보를 초기화하고 다시 읽어오기
    map_data.clear()
    map_data.extend([[ '' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, map_width):
            map_data[i][j] = col[j]
    row_index += map_height

    # 기존의 아군 정보를 초기화하고 다시 읽어오기
    allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0)
        allies[ally_name] = ally
    row_index += num_of_allies

    # 기존의 적군 정보를 초기화하고 다시 읽어오기
    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0)
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    # 기존의 암호문 정보를 초기화하고 다시 읽어오기
    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])

    return map_width, map_height

NICKNAME = '오징어(짬뽕)'
game_data = init(NICKNAME)

# while 반복문: 배틀싸피 메인 프로그램과 클라이언트(이 코드)가 데이터를 계속해서 주고받는 부분
while game_data is not None:
    # 자기 차례가 되어 받은 게임정보를 파싱
    print(f'----입력데이터----\n{game_data}\n----------------')
    parse_data(game_data)

    # 파싱한 데이터를 화면에 출력하여 확인
    print(f'\n[맵 정보] ({len(map_data)} x {len(map_data[0])})')
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            print(f'{map_data[i][j]} ', end='')
        print()

    print(f'\n[아군 정보] (아군 수: {len(allies)})')
    for k, v in allies.items():
        if k == 'A':
            print(f'A (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 메가 포탄: {v[3]}개')
        elif k == 'H':
            print(f'H (아군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (아군 탱크) - 체력: {v[0]}')

    print(f'\n[적군 정보] (적군 수: {len(enemies)})')
    for k, v in enemies.items():
        if k == 'X':
            print(f'X (적군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (적군 탱크) - 체력: {v[0]}')

    print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
    for i in range(len(codes)):
        print(codes[i])


    # 탱크의 동작을 결정하기 위한 알고리즘을 구현하고 원하는 커맨드를 output 변수에 담기
    # 코드 구현 예시: '아래쪽으로 전진'하되, 아래쪽이 지나갈 수 있는 길이 아니라면 '오른쪽로 전진'하라

    '''
    1. 맵 크기 확인
    2. 전차 & 포탑 위치 찾기
    3. 포탑을 향해 발포 가능한 섹터 지정
    4. bfs 탐색을 통해 최단거리로 해당하는 섹터까지 이동
    5. 탐색 중 경로가 막히면 flag 액션을 1회 수행 후 턴을 넘기고 재탐색
    6. 포탑 사격
    7. 암호해독은 못 .. 함 ..
    '''
    from collections import deque

    # map 크기 확인
    def map_size(game_data):
        # 입력 데이터를 행으로 나누기
        game_data_rows = game_data.split('\n')
        row_index = 0

        header = game_data_rows[row_index].split(' ')
        map_height = int(header[0])  # 맵의 세로 크기
        map_width = int(header[1])  # 맵의 가로 크기
        row_index += 1

        return map_width, map_height
    # N = 가로 크기, M = 세로 크기
    N, M = map_size(game_data)
    # print(N, M)

    # 내 전차 위치 찾기
    tank = (-1, -1)
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] == 'A':
                tank = (i, j)
                break
        if tank != (-1, -1):
            break

    # 포탑 찾기
    target = (-1, -1)
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] == 'X':
                target = (i, j)
                break
        if target != (-1, -1):
            break

    # 포탄을 발사 가능 구역
    fire = []

    # 발포가능 구역인지 확인
    def is_passable(field):
        # 해당하는 좌표가 잔디 내 전차의 위치라면 발포 가능
        return field == 'G' or field == 'A'

    # 맵 확인 후 포탄 발사가능 구역 추가
    for i in range(N):
        for j in range(M):
            # 해당 위치에서 발포 불가능이면 skip
            if not is_passable(map_data[i][j]):
                continue

            # 포탑과 같은 행
            if i == target[0] and abs(j - target[1]) <= 3:
                # 포신을 포탑을 향해 회전
                if j < target[1]:
                    dir = "R"
                elif j > target[1]:
                    dir = "L"
                else:
                    continue
                fire.append(((i, j), dir))

            # 포탑과 같은 열
            elif j == target[1] and abs(i - target[0]) <= 3:
                if i < target[0]:
                    dir = "D"
                elif i > target[0]:
                    dir = "U"
                else:
                    continue
                fire.append(((i, j), dir))

    # print(fire)

    new_fire = []
    # 포탄 발사 경로 중 돌이나 나무가 있으면 해당 경로는 제외
    for (fi, fj), fd in fire:
        # print((fi, fj), fd)
        # 오른쪽으로 사격할 때, j+1, j+2, j+3 범위가 유효하면서, 안에 돌멩이 'R'이 있다면 스킵
        if fd == 'R':
            fd_R = []
            for k in range(1, 4):
                nj = fj + k
                if 0 <= nj < N:
                    fd_R.append(map_data[fi][nj])
            # print('fd_r :', fd_R)
            if 'R' not in fd_R and 'T' not in fd_R:
                new_fire.append(((fi, fj), fd))

        # 왼쪽으로 사격할 때
        elif fd == 'L':
            fd_L = []
            for k in range(1, 4):
                nj = fj - k
                if 0 <= nj < N:
                    fd_L.append(map_data[fi][nj])
            # print('fd_l :', fd_L)
            if 'R' not in fd_L and 'T' not in fd_L:
                new_fire.append(((fi, fj), fd))

        # 위쪽으로 사격할 때
        elif fd == 'U':
            fd_U = []
            for k in range(1, 4):
                ni = fi - k
                if 0 <= ni < N:
                    fd_U.append(map_data[ni][fj])
            # print('fd_u :', fd_U)
            if 'R' not in fd_U and 'T' not in fd_U:
                new_fire.append(((fi, fj), fd))

        # 아래쪽으로 사격할 때
        elif fd == 'D':
            fd_D = []
            for k in range(1, 4):
                ni = fi + k
                if 0 <= ni < N:
                    fd_D.append(map_data[ni][fj])
            # print('fd_D :', fd_D)
            if 'R' not in fd_D and 'T' not in fd_D:
                new_fire.append(((fi, fj), fd))

    # print(new_fire)

    action = ['U A', 'D A', 'R A', 'L A', 'S']
    flag = 0

    # 발사 할 수 있는 칸이 없으면 플래그 액션 1회 진행
    if not fire:
        output = action[flag]
        flag = (flag + 1) % 4

    # 발사 할 수 있는 칸이 있으면 가장 해당되는 가까운 칸 까지 bfs 경로 탐색
    else:
        # bfs 탐색
        my_q = deque()
        my_q.append((tank, []))
        visited = set()
        visited.add(tank)
        # 좌표
        found_path = -1
        # 방향
        play_dir = -1

        while my_q:
            # tij = 현재 위치
            tij, path = my_q.popleft()
            # 현재 칸이 후보 칸 중 하나인지 검사
            for fire_i_j, fire_dir in new_fire:
                if tij == fire_i_j:
                    found_path = path
                    play_dir = fire_dir
                    break
            if found_path != -1:
                break

            # 네 방향 확인
            for d, (di, dj) in [['U', (-1, 0)], ['D', (1, 0)], ['L', (0, -1)], ['R', (0, 1)]]:
                ni, nj = tij[0] + di, tij[1] + dj
                if (0 <= ni < N) and (0 <= nj < M):
                    if (ni, nj) not in visited and is_passable(map_data[ni][nj]) or map_data[ni][nj] in ['E1', 'E2', 'E3']:
                        visited.add((ni, nj))
                        my_q.append(((ni, nj), path + [d]))

                    # 해당 칸이 적의 전차라도 추가할 수 있음 (적의 전차는 움직이니까)
                    # if map_data[ni][nj] in ['E1', 'E2', 'E3']: 추후 수정

        # 동작 결정
        if found_path == -1:
            # 후보 칸까지의 경로를 찾지 못하면 플래그 액션 1회 진행
            output = action[flag]
            flag = (flag + 1) % 4

        else:
            if len(found_path) == 0:
                # 발사 가능 칸에 있다면 해당 방향으로 발사
                output = play_dir + ' F'

            else:
                # 발사 지점에 도달하기 위한 최단 경로의 첫 번째 이동 명령을 활용한 이동
                next_move = found_path[0]
                output = next_move + ' A'

    game_data = submit(output)

close()