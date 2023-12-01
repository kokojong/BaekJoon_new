# 백준 17626 Four Squeares 실3

import math
N = int(input())

dp = [0, 1]

for i in range(2, N+1):
    minV = 10**5

    for j in range(1, int(math.sqrt(i)) + 1):
        minV = min(minV, dp[i - j**2] + 1)
    dp.append(minV)

print(dp[N])
