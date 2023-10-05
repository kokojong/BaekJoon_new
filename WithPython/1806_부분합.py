# 백준 1806 부분합 골4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

sums = [0]  # 누적합
for a in arr:
    sums.append(sums[-1] + a)

# print(sums)

l = 1
r = 1
answer = []
while l <= N and r <= N:
    s = sums[r] - sums[l-1]
    if s >= M:
        answer.append(r-l+1)
        l += 1
    else:
        r += 1

if answer:
    print(min(answer))
else:
    print(0)
