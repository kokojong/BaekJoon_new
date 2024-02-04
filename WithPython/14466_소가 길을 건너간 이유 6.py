# 백준 14466 소가 길을 건너간 이유 6 골3

from collections import deque

N, K, R = map(int, input().split())

board = [[0 for _ in range(N)] for _ in range(N)]

roads = []
for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())

    roads.append((r1-1, c1-1, r2-1, c2-1))
    roads.append((r2-1, c2-1, r1-1, c1-1))

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

# print(roads)


def BFS(r, c, k):
    queue = deque()
    queue.append((r, c))
    board[r][c] = k

    while queue:
        qr, qc = queue.popleft()

        for i in range(4):
            rr = qr + dr[i]
            cc = qc + dc[i]

            if 0 <= rr < N and 0 <= cc < N and not board[rr][cc]:
                if (qr, qc, rr, cc) not in roads:
                    board[rr][cc] = k
                    queue.append((rr, cc))


k = 0
for r in range(N):
    for c in range(N):
        if not board[r][c]:
            k += 1
            BFS(r, c, k)

# print(board)

cows = []
for _ in range(K):
    r, c = map(int, input().split())
    cows.append((r-1, c-1))

answer = 0

for i in range(len(cows)):
    for j in range(i+1, len(cows)):
        r1, c1 = cows[i]
        r2, c2 = cows[j]

        if board[r1][c1] != board[r2][c2]:
            answer += 1

print(answer)
