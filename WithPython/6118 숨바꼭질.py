# 백준 6118 숨바꼭질 실1

from collections import deque

N, M = map(int, input().split())

# 헛간 번호, 헛간 거리, 같은 거리를 갖는 헛간의 갯수

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1 for _ in range(N+1)]

queue = deque()
queue.append(1)  # 1로 시작
visited[1] = 0

while queue:
    q = queue.popleft()

    for g in graph[q]:
        if visited[g] == -1:
            queue.append(g)
            visited[g] = visited[q] + 1

maxV = max(visited)

A = N
B = maxV
C = 0
for i in range(1, N+1):
    if visited[i] == maxV:
        A = min(i, A)
        C += 1

print(A, B, C)
