# 백준 1965 상자넣기 실2

N = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
