# 백준 14430 자원 캐기 실2

import sys

input = sys.stdin.readline

R, C = map(int, input().split())

board = []
dp = [[0 for _ in range(C)] for _ in range(R)]

for _ in range(R):
    row = list(map(int, input().split()))
    board.append(row)

for r in range(R):
    for c in range(C):
        dp[r][c] = max(dp[r][c-1], dp[r-1][c]) + board[r][c]

print(dp[-1][-1])
