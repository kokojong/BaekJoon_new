# 백준 10282 해킹 골4

# a가 b에 의존하면 b해킹시 a도 해킹
# 총 몇대가 감염인지, 시간은 얼마인지 구하기

import sys
import heapq

input = sys.stdin.readline

T = int(input())

INF = float('inf')

for _ in range(T):
    N, D, C = map(int, input().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(D):
        a, b, s = map(int, input().split())  # a의 부모가 b
        graph[b].append((a, s))

    visited = [INF for _ in range(N+1)]
    visited[C] = 0  # 시작점

    cnt = 0
    result = 0  # 시간

    # print("visited", visited)
    # print(graph)

    heap = []
    heapq.heappush(heap, (C, 0))  # C에서 시작, cost 0

    while heap:
        now, nowTime = heapq.heappop(heap)

        if nowTime < visited[now]:
            continue  # 갱신 불가

        for next, cost in graph[now]:
            nextTime = nowTime + cost
            if nextTime < visited[next]:  # 갱신 가능
                visited[next] = nextTime
                heapq.heappush(heap, (next, nextTime))

    for v in visited:
        if v < INF:
            cnt += 1  # 감염이 된 애들

            result = max(v, result)

    print(cnt, result)
