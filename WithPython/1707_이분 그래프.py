# 백준 1707 이분 그래프 골4

from collections import deque
import sys
input = sys.stdin.readline


T = int(input())


def bfs(start, group):
    queue = deque()
    queue.append(start)
    visited[start] = group

    while queue:
        q = queue.popleft()

        for g in graphs[q]:
            if not visited[g]:
                queue.append(g)
                visited[g] = -1 * visited[q]

            elif visited[g] == visited[q]:
                return "NO"

    return "YES"


for _ in range(T):
    V, E = map(int, input().split())
    visited = [False for _ in range(V+1)]

    graphs = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        graphs[a].append(b)
        graphs[b].append(a)

    for i in range(1, V+1):
        if not visited[i]:
            result = bfs(i, 1)
            if result == "NO":
                break

    print(result)
