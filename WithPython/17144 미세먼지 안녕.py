# 백준 17144 미세먼지 안녕

from collections import deque
import copy
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

board = []

clean = 0  # 공기 청정기가 끝나는위치(아래부분)
for r in range(R):
    row = list(map(int, input().split()))
    if row[0] == -1:
        clean = r
    board.append(row)


def move():  # 확산
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    global board

    queue = deque()
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                queue.append([r, c])

    newBoard = copy.deepcopy(board)

    while queue:
        qr, qc = queue.popleft()
        go = []  # 퍼져야 하는 애들
        for i in range(4):
            rr = qr + dr[i]
            cc = qc + dc[i]

            if 0 <= rr < R and 0 <= cc < C and board[rr][cc] >= 0:
                go.append([rr, cc])

        l = len(go)
        if l == 0:
            continue

        K = board[qr][qc]//5  # 방향으로 퍼지는 애들의 값
        newBoard[qr][qc] -= K * l  # K씩 l개 만큼 빠진 값으로 변경
        # print("qr, qc, go, k", qr, qc, go, K)
        for rr, cc in go:
            newBoard[rr][cc] += K
    # print("new", newBoard)
    board = newBoard


def turnTop():
    global board
    # 윗부분 0~clean-1 반시계

    top = deque()
    rr = clean-1  # 끝지점
    # 공기 청정기로 들어오는거 부터 시작
    top.append(0)
    for r in range(rr-1, 0, -1):
        top.append(board[r][0])

    for c in range(C-1):
        top.append(board[0][c])

    for r in range(rr):
        top.append(board[r][C-1])

    for c in range(C-1, 0, -1):
        top.append(board[rr][c])

    top.append(top.popleft())
    top.popleft()
    top.append(0)

    for r in range(rr-1, 0, -1):
        board[r][0] = top.popleft()

    for c in range(C-1):
        board[0][c] = top.popleft()

    for r in range(rr):
        board[r][C-1] = top.popleft()

    for c in range(C-1, 0, -1):
        board[rr][c] = top.popleft()


def turnBottom():
    global board

    top = deque()
    rr = clean
    # 공기 청정기로 들어오는거 부터 시작
    top.append(0)
    for c in range(1, C):
        top.append(board[rr][c])

    for r in range(rr+1, R):
        top.append(board[r][C-1])

    for c in range(C-2, -1, -1):
        top.append(board[R-1][c])

    for r in range(R-2, rr, -1):
        top.append(board[r][0])

    # print("bottom", top)
    top.appendleft(0)
    top.pop()
    # print("bottom", top)

    top.popleft()
    for c in range(1, C):
        board[rr][c] = top.popleft()

    for r in range(rr+1, R):
        board[r][C-1] = top.popleft()

    for c in range(C-2, -1, -1):
        board[R-1][c] = top.popleft()

    for r in range(R-2, rr, -1):
        board[r][0] = top.popleft()

    # 아랫부분 clean~R-1 시계
for _ in range(T):
    move()
    # print(board)
    turnTop()
    # print(board)
    turnBottom()
    # print(board)

# 4 3 1
# 0 30 7
# -1 10 0
# -1 0 20
# 0 0 0
answer = 2
for r in range(R):
    answer += sum(board[r])
print(answer)
