# 백준 2482 색상환 골3

N = int(input())
K = int(input())

MOD = 1000000003

# dp[n][k] 1~n까지 색 중에서 k개를 선택하는 경우의 수
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

# n번째 k개 -> n-1에서 k개 선택(n번 미선택) + n-2에서 k-1개 선택(n번을 선택)

for i in range(N+1):
    for j in range(K+1):
        if j == 0:
            dp[i][j] = 1
            continue

        if j == 1:
            dp[i][j] = i
            continue

        dp[i][j] += dp[i-1][j]  # n번 미선택 -> n-1번까지 중 j개 선택

        # n번을 선택 했을 때
        if i == N:
            dp[i][j] += dp[i-3][j-1]  # 끝쪽이라서 i-3
        else:
            dp[i][j] += dp[i-2][j-1]

        dp[i][j] %= MOD
# print(dp)
print(dp[-1][-1])
