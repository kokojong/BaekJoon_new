
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [[False for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    # a > b
    board[a][b] = True

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][k] and board[k][j]:
                board[i][j] = True

answer = 0
for i in range(1, N+1):
    small = 0
    big = 0

    for j in range(1, N+1):
        if i == j:
            continue

        if board[i][j]:
            small += 1

        if board[j][i]:
            big += 1

    if small >= (N)/2 or big >= (N)/2:
        answer += 1

print(answer)
