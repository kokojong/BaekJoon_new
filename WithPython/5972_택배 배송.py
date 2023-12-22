# 백준 5972 택배 배송 골5

import heapq

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
INF = int(10**9)
distance = [INF for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))

heap = []
distance[1] = 0

heapq.heappush(heap, (0, 1))  # cost, node

while heap:
    cost, node = heapq.heappop(heap)

    if distance[node] < cost:
        continue

    for c, next in graph[node]:
        newCost = cost + c

        if newCost < distance[next]:
            distance[next] = newCost
            heapq.heappush(heap, (newCost, next))

print(distance[-1])
