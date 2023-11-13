# 백준 4485 젤다 골4

# [0][0] -> [N-1][N-1] 이동해야함

from collections import deque

INF = float('inf')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 1
while True:
    N = int(input())
    if N == 0:
        break

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    distances = [[INF for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    distances[0][0] = board[0][0]

    while queue:
        qr, qc = queue.popleft()

        for i in range(4):
            rr = qr + dr[i]
            cc = qc + dc[i]

            if 0 <= rr < N and 0 <= cc < N:
                if distances[qr][qc] + board[rr][cc] < distances[rr][cc]:
                    distances[rr][cc] = distances[qr][qc] + board[rr][cc]
                    queue.append((rr, cc))

    print("Problem {0}: {1}".format(cnt, distances[N-1][N-1]))
    cnt += 1
