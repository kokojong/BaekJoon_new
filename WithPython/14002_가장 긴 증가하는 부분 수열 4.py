# 백준 14002 가장 긴 증가하는 부분 수열 4 골4

import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]
stacks = [[arr[i]] for i in range(N)]

# i 입장해서 하나씩 비교해가면서 내가 더 크다면 dp를 갱신
for i in range(1, N):
    for j in range(0, i):
        if arr[i] > arr[j]:
            # dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] < dp[j] + 1:  # 갱신이 필요할때만
                dp[i] = dp[j] + 1
                stacks[i] = stacks[j] + [arr[i]]
answer = max(dp)
for i in range(N):
    if dp[i] == answer:
        print(dp[i])
        print(*stacks[i])
        break
