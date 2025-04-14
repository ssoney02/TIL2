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
    map_data.extend([['' for c in range(map_width)] for r in range(map_height)])
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


NICKNAME = '오세훈(EXO)'
game_data = init(NICKNAME)

delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 상,우,하,좌 탐색
from collections import deque


def bfs(si, sj):
    global ti, tj
    q = deque([(si, sj)])
    visited[si][sj] = 1
    while q:
        location = q.popleft()
        oi, oj = location[0], location[1]
        visited[oi][oj] = 1

        # 목표 지점에 도달하면, break
        # 목표지점이 사거리 안에 들어가면 break
        # for xd in x_delta:
        #     ######### 그냥 매번 네 방향 delta*3범위 만큼 확인해보고 그 안에 x가 있으면 바로 break
        #     # x가 범위 안에 있고, R, T, F가 범위 안에 없어야됨..
        #     ci, cj = oi + xd[0], oj + xd[1]
        #     if 0 <= ci < len(map_data) and 0 <= cj < len(map_data):
        #         if map_data[ci][cj] == 'X':
        #             rti, rtj = ci, cj
        #             print(rti, rtj)
        #             break

        for d in delta:
            ni, nj = oi + d[0], oj + d[1]
            # ni, nj가 범위를 벗어나지 않고, visited==0 이고, W,R,T,F가 아니라면 이동
            if 0 <= ni < len(map_data) and 0 <= nj < len(map_data) and visited[ni][nj] == 0 and map_data[ni][
                nj] not in ['W', 'R', 'T', 'F']:
                q.append((ni, nj))
                route[ni][nj] = (oi, oj)  # 직전에 어디에서 온 건지 경로 기록

    # 목표지점까지 다 도달해서 나왔으면
    # 경로 복원
    final_route = []
    current = route[ti][tj]
    # 목적지에서부터 역으로 되돌아감
    while current is not None:
        final_route.append(current)
        current = route[current[0]][current[1]]

    final_route.reverse()
    print(f'final_route: {final_route}')
    return final_route


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
            mega = v[3]
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

    output = 'A'  # 알고리즘에 의해 커맨드를 결정하기 전 임시로 A 지정

    my_position = [-1, -1]
    # 목표(적군 포탑) 위치 찾기
    for i in range(len(map_data)):
        for j in range(len(map_data)):
            if map_data[i][j] == 'X':
                ti, tj = i, j
                break

    # 나의 현재 위치 찾기
    # 현재위치로부터 목표 지점까지 bfs 돌려서 최단 거리 구하면
    # 지나온 경로 복원
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] == 'A':
                my_position[0] = i
                my_position[1] = j
                break
        if my_position[0] > 0: break

    visited = [[0] * len(map_data) for _ in range(len(map_data))]
    route = [[None] * len(map_data) for _ in range(len(map_data))]

    # bfs로 포탑까지의 최단 경로 찾기
    final = bfs(my_position[0], my_position[1])

    # 커맨드 작성
    # print('final 길이:')
    # print(len(final))
    # print(len(final[0]))
    # print('final[0]')
    # print(final[0])
    outputs = []
    for i in range(len(final)):
        oi, oj = final[i][0], final[i][1]
        # for d in delta:
        if (oi - 3 <= ti <= oi + 3 and oj == tj) or (oi == ti and oj - 3 <= tj <= oj + 3) or i == len(final) - 1:
            # if i == len(final) - 1:
            # 발포 지점에 도달하면, 포탑과의 방향 비교해서 커맨드 전달
            if int(mega) > 0:
                if ti < oi and tj == oj:
                    outputs.append('U F M')
                elif ti == oi and tj > oj:  # 'R F'
                    outputs.append('R F M')
                elif ti > oi and tj == oj:
                    outputs.append('D F M')
                elif ti == oi and tj < oj:
                    outputs.append('L F M')
                break  # 다음 trial로 넘어갔을때 submit에 남아있는거 처리
            else:
                if ti < oi and tj == oj:
                    outputs.append('U F')
                elif ti == oi and tj > oj:  # 'R F'
                    outputs.append('R F')
                elif ti > oi and tj == oj:
                    outputs.append('D F')
                elif ti == oi and tj < oj:
                    outputs.append('L F')
                break  # 다음 trial로 넘어갔을때 submit에 남아있는거 처리

        if i < len(final) - 1:
            ni, nj = final[i + 1][0], final[i + 1][1]
            if ni < oi and nj == oj:
                outputs.append('U A')
            elif ni == oi and nj > oj:
                outputs.append('R A')
            elif ni > oi and nj == oj:
                outputs.append('D A')
            elif ni == oi and nj < oj:
                outputs.append('L A')

    # if my_position[0] < len(map_data) - 1 and map_data[my_position[0] + 1][my_position[1]] == 'G':
    #     output = 'D A'
    # else:
    #     output = 'R A'

    # while 문의 끝에는 다음 코드가 필수로 존재하여야 함
    # output에 담긴 값은 submit 함수를 통해 배틀싸피 메인 프로그램에 전달
    print(outputs)
    # for output in outputs:
    game_data = submit(outputs[0])

# 반복문을 빠져나왔을 때 배틀싸피 메인 프로그램과의 연결을 완전히 해제하기 위해 close 함수 호출
close()