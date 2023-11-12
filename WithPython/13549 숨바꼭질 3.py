# 백준 13549 숨바꼭질 3 골5

import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

INF = float('inf')

visited = [INF for _ in range(100000+1)]

heap = [(0, N)]
visited[N] = 0

while heap:
    # print(heap)
    cost, hq = heapq.heappop(heap)

    if cost > visited[hq]:
        continue

    if hq == K:
        print(visited[hq])
        break

    for h in [hq-1, hq+1, 2*hq]:
        if not 0 <= h < 100001:
            continue

        if visited[h] != INF and visited[h] <= visited[hq]:
            continue

        if h == 2*hq:
            heapq.heappush(heap, (cost, h))
            visited[h] = cost
        else:
            heapq.heappush(heap, (cost+1, h))
            visited[h] = cost+1
