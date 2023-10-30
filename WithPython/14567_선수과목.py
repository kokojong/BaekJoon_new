# 백준 14567 선수과목 골5

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graphs = [[] for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]
answer = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    degrees[b] += 1
    graphs[a].append(b)

# print(graphs)
# print(degrees)

queue = deque()

for i in range(1, N+1):
    if degrees[i] == 0:
        queue.append((i, 1))

while queue:
    q, depth = queue.popleft()

    if degrees[q] == 0:
        answer[q] = depth

    for next in graphs[q]:
        degrees[next] -= 1  # 선행과목 -= 1

        if degrees[next] == 0:
            queue.append((next, depth+1))


# print(answer)

print(" ".join(map(str, answer[1:])))
