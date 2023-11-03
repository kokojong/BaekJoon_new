# 백준 1504 특정한 최단 경로

# 1~N으로 최단거리 이동중 2개의 정점을 포함해야함

import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())

# idea: 1 -> v1 -> v2 -> N or 1 -> v2 -> v1 -> N 중에 작은것

INF = float('inf')


def dijkstra(start, end):
    distance = [INF for _ in range(N+1)]
    heap = []

    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        cost, q = heapq.heappop(heap)

        if distance[q] < cost:
            continue

        for c, next in graph[q]:
            dis = c + cost

            if distance[next] > dis:  # 갱신이 가능하다면
                distance[next] = dis
                heapq.heappush(heap, (dis, next))

    return distance[end]


distance1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
distance2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

answer = min(distance1, distance2)

if answer == INF:
    print(-1)
else:
    print(answer)
