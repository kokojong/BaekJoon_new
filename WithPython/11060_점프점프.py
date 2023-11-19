# 백준 11060 점프점프 실2

from collections import deque

N = int(input())

arr = list(map(int, input().split()))
distance = [-1 for _ in range(N)]

queue = deque()
queue.append(0)
distance[0] = 0

while queue:
    q = queue.popleft()

    for i in range(arr[q]):
        next = q + i + 1

        if next >= N:
            continue

        if distance[next] == -1:
            distance[next] = distance[q] + 1
            queue.append(next)

print(distance[-1])
