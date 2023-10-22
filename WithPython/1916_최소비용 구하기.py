# 백준 1916 최소비용 구하기 골5

import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

INF = int(1e9)
board = [INF for _ in range(N+1)]

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))

start, end = map(int, input().split())

heap = []
board[start] = 0
heapq.heappush(heap, (board[start], start))

while heap:
    cost, h = heapq.heappop(heap)  # 거리, 노드

    if board[h] < cost:  # 갱신 불가 -> 컨티뉴
        continue

    for c, hh in graph[h]:  # 다음 노드까지 거리, 다음 노드 번호
        newCost = cost + c  # 이전까지 + 다음

        if newCost < board[hh]:  # 더 짧은 거리
            # 여기에서 newCost < board[hh] 가 아니라 cost < board[hh]로 써서 메모리 초과가 났다...
            board[hh] = newCost
            heapq.heappush(heap, (newCost, hh))

# print(board)
print(board[end])
