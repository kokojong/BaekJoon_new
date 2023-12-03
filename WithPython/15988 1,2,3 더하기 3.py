# 백준 15988 1,2,3 더하기 3 실2

T = int(input())
k = 10**9 + 9

dp = [0, 1, 2, 4]
for _ in range(T):
    N = int(input())

    for n in range(len(dp), N+1):
        # print("n", n)
        next = dp[n-1] + dp[n-2] + dp[n-3]
        dp.append(next % k)

    print(dp[N] % k)
