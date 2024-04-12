# 백준 2636 치즈 골4

# 모두 녹아서 없어지는데 걸리는 시간,
# 없어지기 1시간 전에 마지막 갯수

from collections import deque

R, C = map(int, input().split())

board = []
total = 0

for _ in range(R):
    row = list(map(int, input().split()))
    board.append(row)
    total += sum(row)

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def BFS(r, c):
    global board

    queue = deque()
    queue.append([r, c])
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[r][c] = True

    melt = 0

    while queue:
        qr, qc = queue.popleft()

        for i in range(4):
            rr = qr + dr[i]
            cc = qc + dc[i]

            if 0 <= rr < R and 0 <= cc < C and visited[rr][cc] == False:
                if board[rr][cc] == 1:
                    board[rr][cc] = 0  # 녹이기, 큐에 넣지 않음
                    visited[rr][cc] = True
                    melt += 1
                else:
                    queue.append([rr, cc])
                    visited[rr][cc] = True

    return melt  # 이만큼 녹임


time = 0

while True:
    result = BFS(0, 0)  # 녹인거의 갯수
    time += 1
    total -= result
    if total == 0:
        print(time)
        print(result)
        break
