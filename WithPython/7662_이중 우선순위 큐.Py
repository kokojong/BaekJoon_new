# 백준 7662 이중 우선순위 큐 골4

from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    t = int(input())

    minhq = []
    maxhq = []
    dic = defaultdict(int)

    for _ in range(t):
        command, k = map(str, input().split())
        k = int(k)

        if command == 'I':
            heapq.heappush(minhq, k)
            heapq.heappush(maxhq, -k)
            dic[k] += 1

        else:
            if not minhq or not maxhq:
                continue

            if k == -1:  # 최솟값 삭제
                # m = heapq.heappop(minhq)
                while minhq:
                    if dic[minhq[0]] > 0:  # 아직 지울수 있는 수이면
                        dic[minhq[0]] -= 1
                        heapq.heappop(minhq)
                        break
                    else:
                        heapq.heappop(minhq)  # 이미 지워졌어야 할 수이면 삭제하고 이어서 진행

            elif k == 1:
                # m = heapq.heappop(maxhq)
                while maxhq:
                    if dic[-maxhq[0]] > 0:  # 아직 지울수 있는 수이면
                        dic[-maxhq[0]] -= 1
                        heapq.heappop(maxhq)
                        break
                    else:
                        heapq.heappop(maxhq)  # 이미 지워졌어야 할 수이면 삭제하고 이어서 진행

    while minhq and dic[minhq[0]] < 1:
        heapq.heappop(minhq)
    while maxhq and dic[-maxhq[0]] < 1:
        heapq.heappop(maxhq)

    if not minhq or not maxhq:
        print('EMPTY')
    else:
        print(-maxhq[0], minhq[0])
