# 백준 2225 합분해 골5

N, K = map(int, input().split())

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]  # K+1개의 숫자로 만들 수 있는 N
dp[1] = [1 for _ in range(N+1)]  # 처음에는 1개를 만들 수 있음!

for i in range(1, K+1):
    # dp[i][j] = dp[i-1][0] ... d[i-1][j]
    for j in range(0, N+1):  # 해당 열 다 돌기
        for k in range(0, j+1):
            dp[i][j] += dp[i-1][k]
        # dp[i][j] += dp[i-1][j]

# print(dp)
print(dp[K][N] % 10 ** 9)
