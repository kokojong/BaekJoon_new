# 백준 2075 N번째 큰 수 실2

import heapq
import sys
input = sys.stdin.readline


N = int(input())

arr = []

heap = []

for _ in range(N):
    row = map(int, input().split())

    for num in row:
        if len(heap) < N:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])

# print(arr)

# index = [N-1 for _ in range(N)]  # 가장 큰것 부터 비교

# for _ in range(N):
#     maxV, maxIdx = -10**8, -1
#     for i in range(N):
#         r = index[i]
#         if arr[r][i] > maxV:
#             maxV = arr[r][i]
#             maxIdx = i

#     # print(maxV, maxIdx)
#     index[maxIdx] -= 1
#     # print(index)

# print(maxV)
