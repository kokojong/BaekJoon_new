# 백준 17484 진우의 달 여행 실3

R, C = map(int, input().split())

board = []

for _ in range(R):
    row = list(map(int, input().split()))
    board.append(row)

INF = float('inf')

dp = [[[0, 0, 0] for _ in range(C)] for _ in range(R)]

for c in range(C):
    for i in range(3):
        dp[0][c][i] = board[0][c]  # [R, D ,L]

for r in range(1, R):
    for c in range(C):
        for i in range(3):
            if (c == 0 and i == 0) or (c == C-1 and i == 2):
                dp[r][c][i] = INF
                continue

            if i == 0:  # R
                dp[r][c][i] = board[r][c] + \
                    min(dp[r-1][c-1][1], dp[r-1][c-1][2])
            elif i == 1:  # D
                dp[r][c][i] = board[r][c] + min(dp[r-1][c][0], dp[r-1][c][2])
            elif i == 2:  # L
                dp[r][c][i] = board[r][c] + \
                    min(dp[r-1][c+1][0], dp[r-1][c+1][1])

answer = INF

for c in range(C):
    answer = min(answer, min(dp[-1][c]))

print(answer)
