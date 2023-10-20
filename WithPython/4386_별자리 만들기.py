# 백준 4386 별자리 만들기 골3

import math
import sys
input = sys.stdin.readline

N = int(input())

stars = []
parents = [i for i in range(N)]
edges = []

for n in range(N):
    a, b = map(float, input().split())
    stars.append([a, b])

# 모든 star간의 거리를 다 구하는건 에바라고 생각했는데 N이 100이라서 가능
for i in range(N-1):
    for j in range(i+1, N):
        x1 = stars[i][0]
        y1 = stars[i][1]
        x2 = stars[j][0]
        y2 = stars[j][1]

        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        edges.append([distance, i, j])

edges.sort()  # 거리가 짧은 순으로 나열


def findParent(x):
    if parents[x] != x:
        parents[x] = findParent(parents[x])

    return parents[x]


answer = 0
for edge in edges:
    dis, x, y = edge

    parentX = findParent(x)
    parentY = findParent(y)

    if parentX != parentY:
        if parentX < parentY:
            parents[parentY] = parentX
        else:
            parents[parentX] = parentY
        answer += dis

print(round(answer, 2))
