# 백준 1644 소수의 연속합 골3

import math
import sys
input = sys.stdin.readline


N = int(input())
sosu = [True for _ in range(N+1)]  # 0 ~ N까지의 소수 여부
sosu[0] = False
sosu[1] = False
for i in range(2, int(math.sqrt(N))+1):
    for j in range(2, N//i + 1):
        # print("i, j", i, j)
        sosu[i * j] = False

sosus = []
totals = [0]  # 누적합
for i in range(N+1):
    if sosu[i]:
        sosus.append(i)
        totals.append(totals[-1] + i)

# print(sosus)
# print(totals)

left = 1
right = 1

answer = 0
while left <= right and right < len(totals):
    total = totals[right] - totals[left-1]  # 부분합
    if total < N:
        right += 1
    elif total > N:
        left += 1
    elif total == N:  # 정답과 같다면 둘다 한칸씩 이동
        answer += 1
        left += 1
        right += 1
print(answer)
