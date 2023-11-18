# 백준 11123 양 한마리... 양 두마리... 실2

from collections import deque

T = int(input())

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def BFS(r, c):
    queue = deque()
    queue.append([r, c])
    board[r][c] = False

    while queue:
        qr, qc = queue.popleft()

        for i in range(4):
            rr = qr + dr[i]
            cc = qc + dc[i]

            if 0 <= rr < R and 0 <= cc < C and board[rr][cc] == True:
                board[rr][cc] = False
                queue.append([rr, cc])


for _ in range(T):
    R, C = map(int, input().split())

    board = [[False for _ in range(C)] for _ in range(R)]

    result = 0

    for r in range(R):
        row = list(input())
        for c in range(C):
            if row[c] == '#':
                board[r][c] = True

    for r in range(R):
        for c in range(C):
            if board[r][c]:
                BFS(r, c)
                result += 1

    print(result)
