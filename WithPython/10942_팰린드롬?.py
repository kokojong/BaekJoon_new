# 백준 10942 팰린드롬? 골4

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

for l in range(2, N):
    for s in range(N - l):
        e = s + l
        if arr[s] == arr[e] and dp[s+1][e-1] == 1:
            dp[s][e] = 1

M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
