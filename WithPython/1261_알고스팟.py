# 백준 1261 알고스팟 골4

from collections import deque
import sys
input = sys.stdin.readline


C, R = map(int, input().split())  # 가로, 세로

board = []

for _ in range(R):
    row = list(map(int, list(str(input().rstrip()))))
    board.append(row)

queue = deque()
queue.append((0, 0))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

answers = [[-1 for _ in range(C)] for _ in range(R)]  # 거기까지 도달하는데 걸리는 크기
answers[0][0] = 0

while queue:
    qr, qc = queue.popleft()

    for i in range(4):
        rr = qr + dr[i]
        cc = qc + dc[i]

        if 0 <= rr < R and 0 <= cc < C and answers[rr][cc] == -1:
            if board[rr][cc] == 0:
                answers[rr][cc] = answers[qr][qc]
                queue.appendleft((rr, cc))  # 안부수고 지나가는게 우선이니까 앞에 넣어줌

            elif board[rr][cc] == 1:
                answers[rr][cc] = answers[qr][qc] + 1  # 부수고 지나감
                queue.append((rr, cc))
print(answers[R-1][C-1])
