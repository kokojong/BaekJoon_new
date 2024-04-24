# 백준 30461 낚시 골4

import sys
input = sys.stdin.readline

R, C, Q = map(int, input().rstrip().split())

board = []
for _ in range(R):
    row = list(map(int, input().rstrip().split()))
    board.append(row)

accums = [[0 for _ in range(C+1)] for _ in range(R+1)]

for r in range(1, R+1):
    for c in range(1, C+1):
        # accums[r][c] = accums[r-1][c-1] + board[r-1][c-1]
        accums[r][c] = accums[r-1][c] + board[r-1][c-1]

dp = [[0 for _ in range(C+1)] for _ in range(R+1)]

for r in range(1, R+1):
    for c in range(1, C+1):
        dp[r][c] = dp[r-1][c-1] + accums[r][c]
# print(dp)


for _ in range(Q):
    W, P = map(int, input().rstrip().split())
    print(dp[W][P])
