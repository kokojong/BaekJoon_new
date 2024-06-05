# 백준 2638 치즈 골3

from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = []
cheezes = []

for _ in range(R):
    row = list(map(int, input().split()))
    board.append(row)

for r in range(R):
    for c in range(C):
        if board[r][c] == 1:
            cheezes.append((r, c))

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def BFS():
    global board
    queue = deque()
    visited = [[False for _ in range(C)] for _ in range(R)]

    queue.append((0, 0))  # 0,0 대입해줌
    board[0][0] = -1
    visited[0][0] = True

    while queue:
        qr, qc = queue.popleft()

        for i in range(4):
            rr = qr + dr[i]
            cc = qc + dc[i]

            if 0 <= rr < R and 0 <= cc < C and (board[rr][cc] == 0 or board[rr][cc] == -1) and visited[rr][cc] == False:
                queue.append((rr, cc))
                board[rr][cc] = -1
                visited[rr][cc] = True
    # print("BFS", board)


def checkCheezes():
    global board
    global cheezes

    left = []
    melt = []
    for cheeze in cheezes:
        r, c = cheeze
        cnt = 0
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            # 면 하나가 닿은거
            if 0 <= rr < R and 0 <= cc < C and board[rr][cc] == -1:
                cnt += 1
        if cnt < 2:
            left.append((r, c))  # 살아남은거
        else:
            # board[r][c] = -1  # 녹은 처리
            melt.append((r, c))  # 녹을거
    for r, c in melt:
        board[r][c] = -1
    cheezes = left
    # print("left chezees, board", cheezes, board)


answer = 0
while cheezes:
    # for _ in range(4):
    BFS()
    checkCheezes()
    answer += 1
print(answer)
