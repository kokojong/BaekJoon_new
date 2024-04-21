# 백준 13565 침투 실2

# 위를 바깥, 아래를 안쪽, 검은색은 못지나감.
from collections import deque

R, C = map(int, input().split())

board = []
for _ in range(R):
    row = list(map(int, input()))
    board.append(row)

# print(board)
visited = [[False for _ in range(C)] for _ in range(R)]


def BFS(r, c):
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    queue = deque()
    queue.append([r, c])
    visited[r][c] = True

    while queue:
        qr, qc = queue.popleft()

        if qr == R-1:
            print("YES")
            exit()

        for i in range(4):
            rr = qr + dr[i]
            cc = qc + dc[i]

            if 0 <= rr < R and 0 <= cc < C and board[rr][cc] == 0 and visited[rr][cc] == False:
                queue.append([rr, cc])
                visited[rr][cc] = True


for r in range(1):
    for c in range(C):
        if board[r][c] == 0 and visited[r][c] == False:
            BFS(r, c)

print("NO")
