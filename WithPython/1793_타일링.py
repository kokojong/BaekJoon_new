# 백준 1793 타일링 실2

dp = [1 for _ in range(251)]

dp[1] = 1
dp[2] = 3

for i in range(3, 251):
    dp[i] = dp[i-1] + 2 * dp[i-2]

while True:
    try:
        n = int(input())
        print(dp[n])

    except:
        break
