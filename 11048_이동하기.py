# 백준 11048 이동하기 실2

# N*M미로에서 4방향 이동가능. N,M에 도착할때의 최대 사탕


N, M = map(int, input().split())

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

board = [list(map(int, input().split())) for _ in range(N)]

for r in range(1, N+1):
    for c in range(1, M+1):
        # dp[r][c] = dp[r-1][c-1] + board[r-1][c-1]
        dp[r][c] = board[r-1][c-1]

for r in range(1, N+1):
    for c in range(1, M+1):
        dp[r][c] = max(dp[r-1][c] + dp[r][c], dp[r][c-1] + dp[r][c])

print(dp[N][M])
