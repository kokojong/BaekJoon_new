# 백준 11066 파일 합치기 골3

# 합치는데 드는 비용 - 두 파일 크기의 합

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    arr = list(map(int, input().split()))

    dp = [[0 for _ in range(k+1)] for _ in range(k+1)]

    for i in range(k-1):
        dp[i][i+1] = arr[i] + arr[i+1]  # 기본 dp (두개를 일단 붙인경우)

        for j in range(i+2, k):
            dp[i][j] = dp[i][j-1] + arr[j]  # 이전에꺼 + j번쨰꺼
        # print("i", i, dp[i])

    for v in range(2, k):
        for i in range(k-v):
            j = i + v

            dp[i][j] += min([dp[i][l] + dp[l+1][j] for l in range(i, j)])

    print(dp[0][k-1])
