# 백준 1753 최단경로 골4
import sys
import copy
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = 10**9
V, E = map(int, input().split())
start = int(input())  # 시작 정점

graph = [[] for _ in range(V+1)]

answer = [INF for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())  # u -> v 가는데 w의 가중치
    graph[u].append((v, w))


def dijkstra(start):
    q = []
    answer[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        weight, now = heapq.heappop(q)

        if answer[now] < weight:  # 이미 더 작다면 continue
            continue

        for end, w in graph[now]:
            if weight + w < answer[end]:
                answer[end] = weight + w
                heapq.heappush(q, (weight + w, end))


dijkstra(start)

# print(answer)

for i in range(1, V+1):
    if answer[i] == INF:
        print('INF')
    else:
        print(answer[i])
