# 백준 2631 줄 세우기 골4

N = int(input())

arr = []
dp = [1 for _ in range(N)]

for _ in range(N):
    arr.append(int(input()))

for i in range(1, N):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 가장 긴 증가하는 수열을 찾고 걔네는 냅두고 나머지를 껴넣으면 최소가 된다

print(N - max(dp))
