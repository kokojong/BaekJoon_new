# 백준 14938 서강그라운드 골4

import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

n, m, r = map(int, input().split())

items = [0] + list(map(int, input().split()))

graph = [[] for i in range(n + 1)]

for i in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((l, b))
    graph[b].append((l, a))

answer = 0

for i in range(1, n+1):
    distance = [INF] * (n+1)

    q = [(0, i)]  # 0의 거리, 나자신
    distance[i] = 0

    while q:
        dis, now = heapq.heappop(q)

        if distance[now] < dis:
            continue

        for c, next in graph[now]:
            cost = dis + c

            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

    tmp = 0
    # print(distance)
    for idx, d in enumerate(distance):
        if d <= m:
            tmp += items[idx]

    answer = max(tmp, answer)

print(answer)
