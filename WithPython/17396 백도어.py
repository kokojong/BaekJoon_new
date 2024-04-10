# 백준 17396 백도어 골5

# 분기점이 N개 있음. 현재는 0이고 목표는 N-1

import heapq
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

# 보이면 1 안보이면 0, -> 안보여야함. 근데 마지막거는 보이는데 갈 수 있다
arr = list(map(int, input().split()))
arr[-1] = 0  # 안보이는 처리(갈 수 있도록)

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))
    graph[b].append((t, a))

INF = float('inf')
visited = [INF for _ in range(N)]
visited[0] = 0

heap = [(0, 0)]  # cost, start

while heap:
    hc, hq = heapq.heappop(heap)

    if visited[hq] < hc:  # 이미 cost보다 낮다면 갱신이 불가
        continue

    for cost, next in graph[hq]:
        newCost = hc + cost

        if newCost < visited[next] and arr[next] == 0:
            visited[next] = newCost
            heapq.heappush(heap, (newCost, next))

if visited[-1] == INF:
    print(-1)
else:
    print(visited[-1])
