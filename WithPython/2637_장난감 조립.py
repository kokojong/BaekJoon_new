# 백준 2637 장난감 조립 골2

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())  # 총 N개, N은 최종 부품
M = int(input())

graphs = [[] for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]
bricks = [[0 for _ in range(N+1)] for _ in range(N+1)]  # 각 블럭별로 필요한 블럭의 수

for _ in range(M):
    X, Y, K = map(int, input().split())  # X를 만드는데 Y가 K개 필요

    graphs[Y].append((X, K))  # Y가 X를 만다는데 K개 들어간다
    degrees[X] += 1

queue = deque()
for i in range(1, N+1):
    if degrees[i] == 0:
        queue.append(i)

while queue:
    q = queue.popleft()

    for next, cnt in graphs[q]:
        if bricks[q].count(0) == N+1:  # 얘를 만드는데 필요한 블럭이 더 없음
            bricks[next][q] += cnt  # next를 만드는데 q가 몇개 필요하다~
        else:
            for i in range(1, N+1):
                bricks[next][i] += (bricks[q][i] * cnt)

        degrees[next] -= 1

        if degrees[next] == 0:
            queue.append(next)

# print(bricks[N])
for i in range(1, N+1):
    if bricks[N][i] > 0:
        print(i, bricks[N][i])
