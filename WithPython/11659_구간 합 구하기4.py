# 백준 11659 구간 합 구하기 4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

sums = [0] * (N+1)  # 누적합

# i 에서 j까지의 합은 sums[j] - sums[i-1]

arr = list(map(int, input().split()))

now = 0
for i in range(N):
    now += arr[i]
    sums[i+1] = now

# print(sums)

for _ in range(M):
    i, j = map(int, input().split())
    print(sums[j] - sums[i-1])
