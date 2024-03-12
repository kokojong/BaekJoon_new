# 백준 2151 거울 설치 골3

# 한쪽문에서 다른쪽 문을 볼수 있도록 거울 설치
# 필요한 거울의 최소 갯수

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

board = []
for _ in range(N):
    row = list(map(str, input().rstrip()))
    board.append(row)

doors = []
for r in range(N):
    for c in range(N):
        if board[r][c] == '#':
            doors.append((r, c))

start = doors[0]
end = doors[1]

# / 거울: 위 -> 오, 아래 -> 왼, 오 -> 위, 왼 -> 아래
# \ 거울: 위 -> 왼, 아래 -> 오, 오 -> 아래, 왼 -> 위

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]  # 위 오 아 왼


def rightMirror(i):
    if i == 0:
        return 1
    if i == 1:
        return 0
    if i == 2:
        return 3
    if i == 3:
        return 2


def leftMirror(i):
    if i == 0:
        return 3
    if i == 1:
        return 2
    if i == 2:
        return 1
    if i == 3:
        return 0


queue = deque()
for i in range(4):
    queue.append((start[0], start[1], 0, i))  # r, c, cnt, dir

while queue:
    r, c, cnt, i = queue.popleft()

    rr = r + dr[i]
    cc = c + dc[i]

    while 0 <= rr < N and 0 <= cc < N and board[rr][cc] != '*':
        if board[rr][cc] == '!':
            queue.append((rr, cc, cnt + 1, rightMirror(i)))
            queue.append((rr, cc, cnt + 1, leftMirror(i)))

        if rr == end[0] and cc == end[1]:
            queue.clear()
            break

        # 다음 칸으로 이동
        rr += dr[i]
        cc += dc[i]
        # print("rr, cc", rr, cc)

print(cnt)
