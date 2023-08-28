# 백준 1699 제곱수의 합 실2

import math
N = int(input())

dp = [100000 for _ in range(N+1)]
dp[0] = 0

for n in range(1, N+1):
    sqr = int(math.sqrt(n))  # 최대로 가능한 제곱수

    for j in range(1, sqr+1):
        dp[n] = min(dp[n], dp[n-j**2] + 1)
    # dp[n] = dp[n - sqr**2] + 1

print(dp[N])
