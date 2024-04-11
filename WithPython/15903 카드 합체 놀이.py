# 백준 15903 카드 합체 놀이 실1

# N장 카드, 두장을 골라서 더하고 두 카드가 다 이 합으로 바뀜
# M번을 하고났을 때 가장 작은 합으로 만드는게 목표

import heapq

N, M = map(int, input().split())

arr = list(map(int, input().split()))

heapq.heapify(arr)
heap = arr

for _ in range(M):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    c = a+b

    heapq.heappush(heap, c)
    heapq.heappush(heap, c)

print(sum(heap))
