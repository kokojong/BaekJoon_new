# 백준 14500 테크노미로 골4

import sys
input = sys.stdin.readline

R, C = map(int, input().split())


def case1(r, c):
    result = [0]

    if c+4 <= C:
        tmp = 0
        for i in range(4):
            tmp += board[r][c+i]
        result.append(tmp)

    if r+4 <= R:
        tmp = 0
        for i in range(4):
            tmp += board[r+i][c]
        result.append(tmp)

    return max(result)


def case2(r, c):
    result = [0]

    if r+2 <= R and c+2 <= C:
        tmp = 0
        for i in range(2):
            for j in range(2):
                tmp += board[r+i][c+j]
        result.append(tmp)
    return max(result)


def case3(r, c):  # 나머지 3개 다 해버리기
    result = [0]

    if r+3 <= R and c+2 <= C:
        # 왼쪽 3개 채우기
        result.append(board[r][c] + board[r+1][c] +
                      board[r+2][c] + board[r][c+1])
        result.append(board[r][c] + board[r+1][c] +
                      board[r+2][c] + board[r+1][c+1])
        result.append(board[r][c] + board[r+1][c] +
                      board[r+2][c] + board[r+2][c+1])

        # 오른쪽 3개 채우기
        result.append(board[r][c+1] + board[r+1][c+1] +
                      board[r+2][c+1] + board[r][c])
        result.append(board[r][c+1] + board[r+1][c+1] +
                      board[r+2][c+1] + board[r+1][c])
        result.append(board[r][c+1] + board[r+1][c+1] +
                      board[r+2][c+1] + board[r+2][c])

        # 지그재그
        result.append(board[r][c] + board[r+1][c] +
                      board[r+1][c+1] + board[r+2][c+1])
        result.append(board[r+1][c] + board[r+2][c] +
                      board[r+1][c+1] + board[r][c+1])

    if r+2 <= R and c+3 <= C:
        # 위 3개 채우기
        result.append(board[r][c] + board[r][c+1] +
                      board[r][c+2] + board[r+1][c])
        result.append(board[r][c] + board[r][c+1] +
                      board[r][c+2] + board[r+1][c+1])
        result.append(board[r][c] + board[r][c+1] +
                      board[r][c+2] + board[r+1][c+2])

        # 아래 3개 채우기
        result.append(board[r+1][c] + board[r+1][c+1] +
                      board[r+1][c+2] + board[r][c])
        result.append(board[r+1][c] + board[r+1][c+1] +
                      board[r+1][c+2] + board[r][c+1])
        result.append(board[r+1][c] + board[r+1][c+1] +
                      board[r+1][c+2] + board[r][c+2])

        # 지그재그
        result.append(board[r][c] + board[r][c+1] +
                      board[r+1][c+1] + board[r+1][c+2])
        result.append(board[r+1][c] + board[r][c+1] +
                      board[r+1][c+1] + board[r][c+2])

    return max(result)


board = []
for _ in range(R):
    row = list(map(int, input().split()))
    board.append(row)

answer = 0
for r in range(R):
    for c in range(C):
        answer = max(answer, case1(r, c), case2(r, c), case3(r, c))

print(answer)
