# 백준 9658 돌게임4 실2

# SK, CY


N = int(input())

dp = [False for _ in range(N+1)]
dp[2] = True

for i in range(4, N+1):
    if dp[i-1] == False:
        dp[i] = True
    if dp[i-3] == False:
        dp[i] = True
    if dp[i-4] == False:
        dp[i] = True


# print(dp)
print('SK' if dp[N] else 'CY')
