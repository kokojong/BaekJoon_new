# 백준 14499 주사위 굴리기 골4

# 주사위에 0이 적혀있고 굴렸는데
# 이동한 칸의 숫자가 0이라면 칸에 주사위 바닥면에 복사
# 0이 아니라면 칸에 적힌 수가 주사위 바닥으로 복사되고 칸이 0이된다

# 주사위놓은곳 좌표, 명령 주고 상단에 쓰여있는 값 구하기

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

N, M, r, c, K = map(int, input().split())

dice = [0, 0, 0, 0, 0, 0]  # 문제에서 주어진 대로 위, 뒤, 오른, 왼, 앞, 바닥

board = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    board[i] = list(map(int, input().split()))

command = list(map(int, input().split()))  # K개


def rollDice(dir):
    # 위, 뒤, 오른, 왼, 앞, 바닥
    global dice
    up, back, right, left, forward, ground = map(int, dice)
    # 동1 서2 북3 남4
    if dir == 1:  # 동쪽으로 가면 뒤, 앞은 그대로
        new = [left, back, up, ground, forward, right]
    elif dir == 2:  # 서쪽도 동일
        new = [right, back, ground, up, forward, left]
    elif dir == 3:  # 왼, 오 동일
        new = [forward, up, right, left, ground, back]
    elif dir == 4:
        new = [back, ground, right, left, up, forward]
    dice = new


for dir in command:
    rr = r + dr[dir - 1]
    cc = c + dc[dir - 1]

    if 0 <= rr < N and 0 <= cc < M:
        r = rr
        c = cc

        rollDice(dir)
        if board[r][c] == 0:
            board[r][c] = dice[5]  # ground
        else:
            dice[5] = board[r][c]
            board[r][c] = 0

        print(dice[0])  # up
