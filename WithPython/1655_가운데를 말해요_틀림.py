# 백준 1655 가운데를 말해요 골2

import heapq
import sys
input = sys.stdin.readline

N = int(input())

heapMax = []
heapMin = []

# 틀린 이유: 1, 2번째 라인을 받으면 바로 print해버림
# i = int(input())
# heapq.heappush(heapMax, (-i, i))  # 최대힙으로 만들고 원래 값을 저장해둔다
# if N == 1:
#     print(i)
#     exit()

# h1 = heapq.heappop(heapMax)
# heapq.heappush(heapMax, (h1))

# i = int(input())
# heapq.heappush(heapMax, (-i, i))
# if N == 2:
#     heapq.heappop(heapMax)
#     print(heapq.heappop(heapMax)[1])
#     exit()

# h1 = heapq.heappop(heapMax)
# h2 = heapq.heappop(heapMax)
# print(h2[1])
# heapq.heappush(heapMax, (h1))
# heapq.heappush(heapMax, (h2))
#


# for i in range(N):
# 시간초과(당연히 그럴줄 암)
# heapq.heappush(heap, int(input()))

# tmp = []
# for _ in range((i+1) // 2):
#     p = heapq.heappop(heap)
#     tmp.append(p)

# print(tmp[-1])

# for _ in range((i+1)//2):
#     p = tmp.pop()
#     heapq.heappush(heap, p)

# idea: 최대heap 과 최소힙을 하나씩 만든다 -> 그 맨 위에꺼를 확인해서 어디에 넣을지 확인하고 넣고 일케하면 될듯?

hMax = heapq.heappop(heapMax)
heapq.heappush(heapMin, (hMax[1], hMax[1]))

# print(heapMax)
# print(heapMin)


for i in range(N):  # N이 2개보다 클때만!
    if i < 2:
        print(h1[1])

    h = int(input())
    # print(heapMax)
    hMax = heapq.heappop(heapMax)
    hMin = heapq.heappop(heapMin)

    heapq.heappush(heapMax, hMax)
    heapq.heappush(heapMin, hMin)

    # min 에 넣어주고 크기에 따라서 평탄화(?)
    heapq.heappush(heapMin, (h, h))
    if len(heapMin) > len(heapMax):
        hMin = heapq.heappop(heapMin)
        heapq.heappush(heapMax, (-hMin[1], hMin[1]))

    # max에서 제일 큰걸 꺼내서 보여주고 다시 넣기
    result = heapq.heappop(heapMax)
    print(result[1])
    heapq.heappush(heapMax, result)
