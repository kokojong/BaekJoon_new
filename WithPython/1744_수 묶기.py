# 백준 1744 수 묶기 골4

import sys
input = sys.stdin.readline

N = int(input())

minus = []
zero = []
plus = []

for _ in range(N):
    k = int(input())

    if k > 0:
        plus.append(k)
    elif k == 0:
        zero.append(k)
    else:
        minus.append(k)


minus.sort()
plus.sort(reverse=True)

answer = 0

for i in range(len(minus)//2):
    answer += (minus[i*2] * minus[i*2+1])
if len(minus) % 2 == 1 and not zero:  # 0이 하나도 없는데 음수가 남음
    answer += minus[-1]

# print(plus)
for i in range(len(plus)//2):
    answer += max(plus[i*2] * plus[i*2+1], plus[i*2] + plus[i*2+1])
if len(plus) % 2 == 1:
    answer += plus[-1]

print(answer)

# 3
# -1
# 1
# 2
# ans = 2 -> 이해안감
# -1 1 2
