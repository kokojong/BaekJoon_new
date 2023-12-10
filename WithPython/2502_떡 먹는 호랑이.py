# 백준 2502 떡 먹는 호랑이 실1

D, K = map(int, input().split())

# D일을 걸려서 K가 되어야하니까

# 1일째, 2일째를 하나씩 완탐으로 넣어보기?

# D일이 걸릴때 최소인 경우 1 1 2 3 ...


dp1 = [0 for _ in range(D+1)]
dp1[1] = 1

for d in range(2, D+1):
    dp1[d] = dp1[d-1] + dp1[d-2]

k = K // dp1[-1]
# print("k", k)

for i in range(1, k+1):
    for j in range(i, K+1):
        dp = [i, j]

        for a in range(2, D):
            dp.append(dp[a-1] + dp[a-2])

        # print("dp", dp)

        if dp[-1] == K:
            print(i)
            print(j)
            exit()
