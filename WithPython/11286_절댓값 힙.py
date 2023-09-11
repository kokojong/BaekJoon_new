# 백준 11286 절댓값 힙 실1

import heapq
import sys
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    x = int(input())

    if x != 0:  # 넣기
        heapq.heappush(heap, (abs(x), x))

    else:  # 꺼내기
        if heap:
            arr = []
            p = heapq.heappop(heap)
            arr.append(p[1])

            while heap and heap[0][0] == p:  # 절댓값이 같다면
                arr.append(heapq.heappop(heap)[1])
            arr.sort(reverse=True)
            print(arr.pop())

            while arr:
                a = arr.pop()
                heapq.heappush(heap, (abs(a), a))

        else:
            print(0)
