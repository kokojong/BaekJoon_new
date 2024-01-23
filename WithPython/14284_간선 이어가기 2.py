# 백준 14284 간선 이어가기 2 골5

import heapq

n, m = map(int, input().split())

INF = float('inf')
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())  # a 와 b가 연결, c의 가중치(무방ㅇ향)
    graph[a].append((c, b))
    graph[b].append((c, a))

start, end = map(int, input().split())

heap = []

arr = [INF for _ in range(n+1)]
arr[start] = 0

heapq.heappush(heap, (0, start))

while heap:
    cost, h = heapq.heappop(heap)

    if arr[h] < cost:
        continue

    for c, next in graph[h]:
        newCost = cost + c

        if newCost < arr[next]:
            arr[next] = newCost
            heapq.heappush(heap, (newCost, next))

# print(arr)
print(arr[end])
