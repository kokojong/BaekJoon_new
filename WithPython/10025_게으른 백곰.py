# 백준 10025 게으른 백곰 실3

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# 좌우로 K개만큼 가져갈 수 있음

ices = [0 for _ in range(1000001)]
for _ in range(N):
    g, x = map(int, input().split())
    ices[x] = g

end = 2*K + 1
window = sum(ices[:end])
answer = window

for i in range(end, 1000001):
    window += (ices[i] - ices[i-end])
    answer = max(answer, window)

print(answer)
