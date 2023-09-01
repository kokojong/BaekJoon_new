# 백준 1655 가운데를 말해요 골2

import heapq
import sys
input = sys.stdin.readline

N = int(input())

heapMax = []
heapMin = []

# 틀린 이유: 1, 2번째 라인을 받으면 바로 print해버림
# 또한 크기가 다를때만 평탄화 하게 했는데
# 1 2 5 0 순으로 들어온다고 하면
# [1, 2] [5] 일때 0이 들어오면 max heap에 들어가야하는데 안된다!

# 알게된 것! heap에 [0]은 접ㅇ근이 가능하다! 그래서 pop하고 Push할 필요가 없다

for i in range(N):
    h = int(input())

    if len(heapMax) == len(heapMin):
        heapq.heappush(heapMax, (-h, h))
    else:
        heapq.heappush(heapMin, (h, h))

    if heapMax and heapMin and heapMax[0][1] > heapMin[0][1]:  # 다시 정렬해야한다면
        hMax = heapq.heappop(heapMax)[1]
        hMin = heapq.heappop(heapMin)[1]

        heapq.heappush(heapMax, (-hMin, hMin))
        heapq.heappush(heapMin, (hMax, hMax))

    print(heapMax[0][1])
