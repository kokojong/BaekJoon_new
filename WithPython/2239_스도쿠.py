# 백준 2239 스도쿠 골4

import sys
input = sys.stdin.readline

board = []

for i in range(9):
    row = list(map(int, input().rstrip()))
    board.append(row)

zeros = []
for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            zeros.append((r, c))


def checkRow(r, num):  # 행 체크 num - board에서 해당 위치의 숫자
    for i in range(9):
        if board[r][i] == num:
            return False
    return True


def checkColumn(c, num):
    for i in range(9):
        if board[i][c] == num:
            return False
    return True


def checkBox(r, c, num):
    rr = r//3 * 3
    cc = c//3 * 3

    for i in range(3):
        for j in range(3):
            if board[rr+i][cc+j] == num:
                return False
    return True


def dfs(depth):
    if depth == len(zeros):
        for r in range(9):
            for c in range(9):
                print(board[r][c], end="")
            print()
        exit()

    r, c = zeros[depth]

    for n in range(1, 10):
        if checkRow(r, n) and checkColumn(c, n) and checkBox(r, c, n):
            board[r][c] = n
            dfs(depth+1)
            board[r][c] = 0


dfs(0)
