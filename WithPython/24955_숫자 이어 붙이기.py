# 백준 24955 숫자 이어 붙이기 골4

from collections import deque
import sys
input = sys.stdin.readline


N, Q = map(int, input().split())  # N: 집의 개수, Q: 놀이할 횟수
houses = [0]
for num in map(int, input().split()):
    houses.append(num)

graph = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)


def addTwo(a, b):
    strA = str(a)
    strB = str(b)
    return int(strA + strB) % 1_000_000_007


def bfs(s, e, houses, graph):
    visited = [-1 for _ in range(N+1)]
    queue = deque()
    queue.append(s)
    visited[s] = houses[s]

    while queue:
        q = queue.popleft()

        for g in graph[q]:
            if visited[g] == -1:
                visited[g] = addTwo(visited[q], houses[g])  # 두개의 숫자를 더해서 넣어주기
                queue.append(g)
    # print("visited", visited)
    return visited[e]


for _ in range(Q):
    start, end = map(int, input().split())
    print(bfs(start, end, houses, graph))
