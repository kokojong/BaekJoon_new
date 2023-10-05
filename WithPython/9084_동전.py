# 백준 9084 동전 골5

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0 for _ in range(M+1)]
    dp[0] = 1

    for i in range(M+1):
        if i % coins[0] == 0:
            dp[i] = 1

    for n in range(1, N):
        for i in range(M+1):
            coin = coins[n]
            if i >= coin:
                dp[i] = dp[i-coin] + dp[i]
    print(dp[-1])
