# 백준 15989 1,2,3 더하기 4 골5

dp = [1 for _ in range(10001)]

for i in range(2, 10001):
    dp[i] += dp[i-2]

for i in range(3, 10001):
    dp[i] += dp[i-3]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])
