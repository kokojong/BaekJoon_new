# 백준 16948 데스 나이트 실1

from collections import deque

N = int(input())

r1, c1, r2, c2 = map(int, input().split())
INF = float('inf')
board = [[INF for _ in range(N)] for _ in range(N)]
# visited = [[False for _ in range(N)] for _ in range(N)]

queue = deque()
queue.append((0, r1, c1))
board[r1][c1] = 0
# visited[r1][c1] = True

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

while queue:
    cost, r, c = queue.popleft()

    for i in range(6):
        rr = r + dr[i]
        cc = c + dc[i]

        if 0 <= rr < N and 0 <= cc < N and board[rr][cc] == INF:
            board[rr][cc] = cost + 1
            queue.append((cost+1, rr, cc))

if board[r2][c2] == INF:
    print(-1)
else:
    print(board[r2][c2])
