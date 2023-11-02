# 백준 1922 네트워크 연결 골4

# 모든 컴퓨터가 연결이 되어있어야한다.

import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
heap = []

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == b:
        continue
    graph[a].append((c, b))
    graph[b].append((c, a))

for i in range(1, N+1):
    for g in graph[i]:
        heapq.heappush(heap, (g[0], i, g[1]))  # i와 g[1]연결, 그 길이는 g[0]

parents = [i for i in range(N+1)]
answer = 0


def findParent(x):
    if parents[x] != x:
        parents[x] = findParent(parents[x])

    return parents[x]


while heap:
    c, a, b = heapq.heappop(heap)
    # print("h", c, a, b)

    pA = findParent(a)
    pB = findParent(b)

    if pA == pB:
        continue

    if pA < pB:
        parents[pB] = pA
    else:
        parents[pA] = pB

    answer += c
    # print("a, b, c, answer", a, b, c, answer)

print(answer)
