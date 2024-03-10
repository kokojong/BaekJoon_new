# 백준 1021 회전하는 큐 실3

from collections import deque

N, M = map(int, input().split())

arr = list(map(int, input().split()))

queue = deque([i for i in range(1, N+1)])

idx = 0

answer = 0
for a in arr:
    while True:
        if queue[0] == a:
            queue.popleft()
            break

        if queue.index(a) < len(queue)/2:  # 왼쪽에 더 가까우면
            while queue[0] != a:
                queue.append(queue.popleft())
                answer += 1
        else:
            while queue[0] != a:
                queue.appendleft(queue.pop())
                answer += 1

print(answer)
