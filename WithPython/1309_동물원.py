# 백준 1309 동물원 실1

N = int(input())

dp = [[0, 0, 0], [1, 1, 1]]

for i in range(2, N+1):
    tmp = [0, 0, 0]  # 없, 왼, 오
    tmp[0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    tmp[1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    tmp[2] = (dp[i-1][0] + dp[i-1][1]) % 9901

    dp.append(tmp)

print(sum(dp[-1]) % 9901)
