# 백준 1660 캡틴 이다솜 실1

from sys import stdin

n = int(stdin.readline())
arr = []
num = 0
i = 1

while n > num:
    num += (i * (i + 1)) // 2
    arr.append(num)
    i += 1

dp = [int(1000000) for i in range(n + 1)]
for i in range(1, n + 1):
    for num in arr:
        if num == i:
            dp[i] = 1
            break
        elif num > i:
            break
        dp[i] = min(dp[i], 1 + dp[i - num])

print(dp[n])
