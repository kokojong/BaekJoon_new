# 백준 7576 토마토 골5

from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())  # M: 가로, N: 세로

# 1 - 익은 토마토, 0 - 익지 않은 토마토, -1 - 토마토가 들어있지 않음

board = []

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

queue = deque([])

for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            queue.append((r, c))


def checkBoard(board):
    for r in range(N):
        for c in range(M):
            if board[r][c] == 0:
                return False  # 하나라도 익지 않은게 있으면 false

    return True


def checkMax(board):
    maxV = 0
    for row in board:
        maxV = max(maxV, max(row))

    return maxV - 1


def bfs(board):

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while queue:
        r, c = queue.popleft()  # r, c

        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0 <= rr < N and 0 <= cc < M and board[rr][cc] == 0:
                board[rr][cc] = board[r][c] + 1
                queue.append((rr, cc))

    if checkBoard(board):  # 이미 다 익은 경우
        return checkMax(board)
    # 실수했던 부분: queue를 돌때마다 check를 해버려서 시간초과가 발생했다.
    # 모든 queue를 다 pop 하고서야 체크해줌으로 마무리!

    return -1


print(bfs(board))
