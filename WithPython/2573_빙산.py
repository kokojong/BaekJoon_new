# 백준 2573 빙산 골4

from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())  # 행, 열

board = []

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def check(bing):
    visited = [[False for _ in range(M)] for _ in range(N)]

    cnt = 0

    for r in range(N):
        for c in range(M):
            if bing[r][c] > 0 and not visited[r][c]:
                queue = deque()
                queue.append((r, c))
                visited[r][c] = True
                cnt += 1

                while queue:
                    qr, qc = queue.popleft()
                    for i in range(4):
                        rr = qr + dr[i]
                        cc = qc + dc[i]

                        if 0 <= rr < N and 0 <= cc < M and bing[rr][cc] > 0 and not visited[rr][cc]:
                            visited[rr][cc] = True
                            queue.append((rr, cc))

    # print("cnt", cnt)  # 연결된 빙산의 갯수

    return cnt


answer = 0
while True:
    answer += 1

    minus = [[0 for _ in range(M)] for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if board[r][c] <= 0:
                continue

            for i in range(4):
                rr = r + dr[i]
                cc = c + dc[i]

                if 0 <= rr < N and 0 <= cc < M and board[rr][cc] <= 0:
                    minus[r][c] -= 1

    for r in range(N):
        for c in range(M):
            board[r][c] = board[r][c] + minus[r][c]

    flag = False
    for r in range(N):
        for c in range(M):
            if board[r][c] > 0:
                flag = True  # 얼음이 남아있는지 체크
                break
    if not flag:
        break

    if check(board) >= 2:
        print(answer)
        exit()

print(0)
