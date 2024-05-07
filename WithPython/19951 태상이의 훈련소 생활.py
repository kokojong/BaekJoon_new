# 백준 19951 태상이의 훈련소 생활 골5
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
accums = [0 for _ in range(N+1)]

for _ in range(M):
    a, b, k = map(int, input().split())
    accums[a-1] += k
    accums[b] -= k

# print(accums)
i = 1
now = accums[i-1]

while i < N:
    accums[i] += now
    now = accums[i]
    i += 1
# print(accums)
for i in range(N):
    arr[i] += accums[i]

print(*arr)
