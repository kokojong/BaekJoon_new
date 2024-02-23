# 백준 11568 민균이의 계략 실2

# 순증가가 아니면 바보라고 놀림 (같은것도) + 원소의 갯수가 제일 많은 수열이어야만 함!

# 수열의 원소의 최대 갯수(가장 긴 수열의 길이!)
# 가장 긴 증가하는 수열!

N = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N):  # i번째가 마지막일때
    max_val = 0
    for j in range(i):  # 그 앞에를 하나씩 체크
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)  # j까지에서 1개 더 올라간거랑 비교

print(max(dp))
