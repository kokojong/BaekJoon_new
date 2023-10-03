# 백준 27172 수 나누기 게임 골5

# 숫자 1~100만
# 내 카드로 나눠 떨어지면 승리. 둘다 아니라면 무승부
# 본인을 제외한 모든 사람들과 결투

# 모든 플레이어의 점수

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

scores = [0 for _ in range(10**6+1)]
visited = [False for _ in range(10**6+1)]

for a in arr:
    visited[a] = True

for i in sorted(arr):
    for j in range(i*2, 10**6+1, i):
        if visited[j]:
            scores[i] += 1
            scores[j] -= 1

for num in arr:
    print(scores[num], end=" ")


# for i in range(N):
#     for j in range(i+1, N):
#         l = arr[i]
#         r = arr[j]

#         if l % r == 0:
#             scores[j] += 1
#             scores[i] -= 1
#         elif r % l == 0:
#             scores[i] += 1
#             scores[j] -= 1

# print(' '.join(map(str, scores)))
