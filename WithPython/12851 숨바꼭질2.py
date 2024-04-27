# 백준 12851 숨바꼭질2 골4

from collections import deque
N, K = map(int, input().split())

# +1 -1 *2

visited = [False for _ in range(100000+1)]
visited[N] = True

queue = deque()
queue.append((0, N))

answer = [100000, 0]  # 몇초, 몇가지

while queue:
    time, now = queue.popleft()

    visited[now] = True

    if now == K:
        # print("time", time, now, queue)
        if answer[0] == 100000:
            answer[0] = time
            answer[1] += 1
        elif time == answer[0]:
            answer[1] += 1
        # break

    for k in [-1, 1, now]:
        next = now + k
        if 0 <= next <= 100000 and visited[next] == False and time <= answer[0]:
            # visited[next] = True
            queue.append((time+1, next))

for a in answer:
    print(a)
