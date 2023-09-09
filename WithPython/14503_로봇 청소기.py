# 백준 14503 로봇 청소리 골4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []

r, c, d = map(int, input().split())

for _ in range(N):
    board.append(list(map(int, input().split())))

# print(board)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 0 빈칸, 1 벽

answer = 0


def checkDir(r, c):
    # 하나라도 청소 가능한 방이 있는지 체크
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        if 0 <= rr < N and 0 <= cc < M and board[rr][cc] == 0:
            return True

    return False


while True:
    if board[r][c] == 0:
        board[r][c] = -1  # 청소처리
        answer += 1

    if checkDir(r, c) == False:
        dd = (d+2) % 4  # 빠꾸
        rr = r + dr[dd]
        cc = c + dc[dd]

        if board[rr][cc] == 1:
            print(answer)
            exit()
        else:
            r = rr
            c = cc

    else:
        d = (d-1) % 4  # 회전
        rr = r + dr[d]
        cc = c + dc[d]

        if 0 <= rr < N and 0 <= cc < M and board[rr][cc] == 0:
            # 전진
            r = rr
            c = cc
