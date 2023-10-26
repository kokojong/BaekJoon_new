# 백준 16929 Two dots 골4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def DFS(depth, r, c, alpha, startR, startC):
    if depth >= 4 and r == startR and c == startC:  # 사이클 형성 - 이미 방문했던거라면
        print("Yes")
        exit()

    # visited[r][c] = True // 빼야하는 이유 - 복원하는 과정이랑 상관없이 방문처리를 해버림

    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        if not (0 <= rr < N and 0 <= cc < M) or board[rr][cc] != alpha:
            continue

        if not visited[rr][cc]:
            visited[rr][cc] = True
            DFS(depth + 1, rr, cc, alpha, startR, startC)
            visited[rr][cc] = False


for r in range(N):
    for c in range(M):
        DFS(1, r, c, board[r][c], r, c)

print("No")
