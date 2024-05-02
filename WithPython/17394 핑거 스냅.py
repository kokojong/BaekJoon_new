# 백준 17394 핑거 스냅 골5

from collections import deque

T = int(input())

sosus = [True for _ in range(100000+1)]

sosus[0] = False
sosus[1] = False

for i in range(2, 100000+1):
    for j in range(2, 100000//i+1):
        sosus[i * j] = False

# print(sosus[:30])

for _ in range(T):
    N, A, B = map(int, input().split())

    visited = [False for _ in range(3000000+1)]
    visited[N] = True
    queue = deque()
    queue.append((0, N))

    isPosible = False

    while queue:
        c, q = queue.popleft()

        if A <= q <= B and sosus[q] == True:
            isPosible = True
            print(c)
            break

        for next in [q//2, q//3, q-1, q+1]:
            if 0 <= next <= 3000000 and visited[next] == False:
                queue.append((c+1, next))
                visited[next] = True

    if not isPosible:
        print(-1)
