# 백준 9252 LCS 2 골4

import sys
input = sys.stdin.readline

s1 = [""] + list(input().rstrip())
s2 = [""] + list(input().rstrip())

dp = [['' for _ in range(len(s2))] for _ in range(len(s1))]

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + s1[i]

        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[-1][-1]))
if len(dp[-1][-1]) != 0:
    print(dp[-1][-1])
