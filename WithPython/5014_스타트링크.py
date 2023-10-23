# 백준 5014 스타트링크 실1

from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

visited = [False for _ in range(F+1)]

visited[S] = True

queue = deque()
queue.append((S, 0))

while queue:
    q, dis = queue.popleft()
    if q == G:
        print(dis)
        exit()

    if q + U <= F and not visited[q+U]:
        visited[q + U] = True
        queue.append((q + U, dis + 1))

    if q - D >= 1 and not visited[q - D]:
        visited[q - D] = True
        queue.append((q - D, dis + 1))

print("use the stairs")
