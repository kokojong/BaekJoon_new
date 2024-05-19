# 백준 11279 최대힙 실2

import heapq
import sys

input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    K = int(input())

    if K == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -K)
