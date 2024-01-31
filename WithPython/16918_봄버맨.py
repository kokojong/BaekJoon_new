# 백준 16918 봄버맨 실1

# 폭탄은 3초후에 폭발, 인접한 애들까지 파괴되어 빈칸이 된다
# 폭탄 옆에 폭탄이 있다면 폭발없이 파괴 -> 연쇄반응x

import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())

board = []
time = 0

for _ in range(R):
    row = []
    for l in list(input().rstrip()):
        if l == '.':
            row.append(-1)
        else:
            row.append(3)
    board.append(row)

time += 1  # 1초간 암것도 안함
for r in range(R):
    for c in range(C):
        if board[r][c] > 0:
            board[r][c] -= 1  # 남은 시간이 흐름

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

while True:
    for r in range(R):
        for c in range(C):
            if board[r][c] == -1:
                board[r][c] = 3  # 빈곳에 폭탄 설치
            else:
                board[r][c] -= 1

    time += 1
    # print("time", time)
    # print(board)

    if time == N:
        break

    queue = []
    for r in range(R):
        for c in range(C):
            if board[r][c] == 1:  # 1초 남은게 있다면
                board[r][c] = -1
                queue.append((r, c))
            elif board[r][c] > 0:
                board[r][c] -= 1

    while queue:
        r, c = queue.pop()

        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0 <= rr < R and 0 <= cc < C:
                board[rr][cc] = -1  # 차괴해서 비움

    time += 1
    # print("time", time)
    # print(board)
    if time == N:
        break

for r in range(R):
    row = []
    for c in range(C):
        if board[r][c] >= 0:
            row.append("O")
        else:
            row.append(".")
    print(''.join(row))
