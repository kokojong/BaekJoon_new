# 백준 10021 Watering the Fields 골3

# N개의 밭
# cost는 (r1 - r2) ^ 2 + (c1 - c2) ^ 2
# 최소값으로 하려고 함
# 근데 cost가 C이상어야만 설치함

import sys
import heapq
input = sys.stdin.readline

N, C = map(int, input().split())

board = []

for _ in range(N):
    r, c = map(int, input().split())
    board.append((r, c))

heap = []

for i in range(N):
    for j in range(i+1, N):
        cost = (board[i][0] - board[j][0])**2 + (board[i][1] - board[j][1])**2
        if cost >= C:
            heapq.heappush(heap, (cost, i, j))  # i랑 j를 잇는 간선이 cost의 가중치

parents = [i for i in range(N)]


def findParents(x):
    if parents[x] != x:
        parents[x] = findParents(parents[x])

    return parents[x]


answer = 0
unioned = 0  # 연결이 된게 몇개인지

while heap:
    cost, i, j = heapq.heappop(heap)

    ii = findParents(i)
    jj = findParents(j)

    if ii == jj:
        continue

    if ii < jj:
        parents[jj] = parents[ii]
    else:
        parents[ii] = parents[jj]

    unioned += 1
    answer += cost

    if unioned == N-1:
        break

if unioned == N-1:
    print(answer)
else:
    print(-1)
