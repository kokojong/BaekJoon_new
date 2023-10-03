# 백준 17404 RGB 거리 2 골4

import sys
input = sys.stdin.readline

N = int(input())

INF = float('inf')

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

answer = INF

for i in range(3):
    dp = [[INF, INF, INF] for _ in range(N)]  # 처음에 고른거 기준
    dp[0][i] = arr[0][i]

    for j in range(1, N):
        dp[j][0] = arr[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = arr[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = arr[j][2] + min(dp[j-1][0], dp[j-1][1])

    for k in range(1, 3):
        kk = (i+k) % 3  # 본인거 제외한거
        answer = min(answer, dp[-1][kk])

print(answer)
