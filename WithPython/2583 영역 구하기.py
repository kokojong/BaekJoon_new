# 백준 2583 영역 구하기 실1

from collections import deque
R, C, K = map(int, input().split())

board = [[0 for _ in range(C)] for _ in range(R)]  # visited처럼 사용
answer = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    # 0 2 4 4

    r1 = R - 1 - y1
    c1 = x1

    r2 = R - y2
    c2 = x2

    for rr in range(r2, r1+1):
        for cc in range(c1, c2):
            board[rr][cc] = 1


def BFS(r, c):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    result = []

    queue = deque()
    queue.append((r, c))
    result.append((r, c))

    global board
    board[r][c] = 1

    while queue:
        qr, qc = queue.popleft()

        for i in range(4):
            rr = qr + dr[i]
            cc = qc + dc[i]

            if 0 <= rr < R and 0 <= cc < C and board[rr][cc] == 0:
                board[rr][cc] = 1
                queue.append((rr, cc))
                result.append((rr, cc))

    return result


for r in range(R):
    for c in range(C):
        if board[r][c] == 0:
            answer.append(len(BFS(r, c)))

answer.sort()

print(len(answer))
print(*answer)
