# 백준 11057 오르막 수 실1

# 수의 자리가 오름차순을 이루는 수 2234 3678 11119

N = int(input())

# new +   이미 오름차순
# ex) 2 234 이런식 -> 즉 맨 앞자리 숫자 이하만 가능

dp = [1 for _ in range(10)]  # 각 숫자가 맨 앞에 온 경우의 수
# 0 ~ 9까지

for _ in range(N-1):
    for j in range(1, 10):  # 1 ~9
        # dp[j] = int((j+2) * (j+1) / 2)
        dp[j] += dp[j-1]

print(sum(dp) % 10007)
