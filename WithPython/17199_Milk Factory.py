# 백준 17199 Milk Factory 실1

# N개의 stations 1~N, N-1 간선
# 컨베이어 벨트가 단방향
# i으로는 모두 여행(?) 가능한 경우를 찾기

from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())  # a -> b로 가는거라서 반대로 b로 향하는게 a로 구현
    graph[b].append(a)


def BFS(x):
    queue = deque()

    visited = [False for _ in range(N+1)]

    queue.append(x)
    visited[x] = True

    while queue:
        q = queue.popleft()

        for g in graph[q]:
            if not visited[g]:
                queue.append(g)
                visited[g] = True

    for i in range(1, N+1):
        if not visited[i]:
            return False

    return True


for i in range(1, N+1):
    if BFS(i):
        print(i)
        exit()

print(-1)
