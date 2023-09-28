# 백준 1238 파티 골3

# N개의 마을에 1명씩 삼 - 학생, X번에 모여서 파티하기. 총 M개의 단방향 도로, Ti시간 소요(cost)

# X에 왔다가 다시 집으로 되돌아가는데 그중에 가장 많은 시간 소비하는 학생 찾기

import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

INF = int(1e9)

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))


def dijk(start):
    distance = [INF for _ in range(N+1)]
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        cost, now = heapq.heappop(heap)

        if distance[now] < cost:
            continue  # 개선의 여지가 없으면 pass

        for g in graph[now]:  # end, cost
            if cost + g[1] < distance[g[0]]:  # 기존의 경로보다 작다면
                distance[g[0]] = cost + g[1]
                heapq.heappush(heap, (distance[g[0]], g[0]))  # newCost, end
    return distance


answer = 0
for i in range(1, N+1):
    value = dijk(i)[X] + dijk(X)[i]  # 왔다가 가는 경로의 합
    if value > answer:
        answer = value
print(answer)
