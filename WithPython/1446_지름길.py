# 백준 1446 지름길 실1

N, D = map(int, input().split())

arr = []
dp = [i for i in range(D+1)]

for _ in range(N):
    s, e, l = map(int, input().split())
    arr.append((s, e, l))

arr.sort()

for s, e, l in arr:
    if e > D:
        continue
    dp[e] = min(dp[e], dp[s] + l)
    for i in range(e+1, D+1):
        dp[i] = min(dp[i], dp[i-1] + 1)

print(dp[-1])
