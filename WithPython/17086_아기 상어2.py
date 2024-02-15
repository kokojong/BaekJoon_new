# 백준 17086 아기 상어2 실2

# N*M 공간에 상어 여러마리
# 안전거리 - 가장 가까운 아기 상어와의 거리 - 다른칸으로 가기 위해서 지나야 하는 칸의 수, 8방향 가능
# 안전 거리가 가장 큰 칸을 찾기

# 1 3
# 1 0 0

from collections import deque

R, C = map(int, input().split())

board = []

for r in range(R):
    row = list(map(int, input().split()))
    board.append(row)

dr = [-1, -1, -1, 0, 1, 1, 1, 0]  # 왼쪽위 -> 위 ...
dc = [-1, 0, 1, 1, 1, 0, -1, -1]


def findShark(r, c):
    visited = [[False for _ in range(C)] for _ in range(R)]

    queue = deque()
    queue.append((r, c, 0))
    visited[r][c] = True

    while queue:
        qr, qc, k = queue.popleft()

        for i in range(8):
            rr = qr + dr[i]
            cc = qc + dc[i]

            if 0 <= rr < R and 0 <= cc < C and not visited[rr][cc]:
                queue.append((rr, cc, k+1))
                visited[rr][cc] = True
                if board[rr][cc]:
                    return k+1


answer = 0

for r in range(R):
    for c in range(C):
        if board[r][c]:
            continue

        result = findShark(r, c)
        answer = max(result, answer)

print(answer)
