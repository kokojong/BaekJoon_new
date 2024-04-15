# 백준 3020 개똥벌레 골5

from collections import Counter
import sys
input = sys.stdin.readline

# 아래, 위 순서대로 반복함.
N, H = map(int, input().split())  # N이 길이(짝수), H가 높이
# 20만 50만
# 하나씩 다해보면 100억 -> 시간초과

top = [0 for _ in range(H+1)]
bottom = [0 for _ in range(H+1)]

for i in range(N):
    k = int(input())
    if i % 2 == 0:
        bottom[k] += 1
    else:
        top[k] += 1

for i in range(H-1, 0, -1):  # 1 ~ H-1
    top[i] += top[i+1]
    bottom[i] += bottom[i+1]

# print(top)
# print(bottom)

answers = []
for i in range(1, H+1):
    r = top[H-i+1] + bottom[i]
    answers.append(r)

M = min(answers)  # 가장 작은거
C = Counter(answers)[M]

print(M, C)
