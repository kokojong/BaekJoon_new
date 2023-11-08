# 백준 11779 최소비용 구하기2 골3

import heapq
import sys
input = sys.stdin.readline


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())

INF = float('inf')


def dijkstra(start, end):
    distance = [INF for _ in range(N+1)]
    routes = [[i] for i in range(N+1)]
    heap = []

    heapq.heappush(heap, (0, start, [start]))  # 비용, 시작, 경로
    distance[start] = 0

    while heap:
        dis, q, route = heapq.heappop(heap)

        if dis > distance[q]:
            continue

        for c, b in graph[q]:
            cost = dis + c

            if cost < distance[b]:
                distance[b] = cost
                routes[b] = route + [b]
                heapq.heappush(heap, (cost, b, route + [b]))

    print(distance[end])
    print(len(routes[end]))
    print(*routes[end])


dijkstra(start, end)
