# 백준 9177 단어 섞기 골4

from collections import deque

T = int(input())

# 1000 * (200 + 200)
for i in range(T):
    A, B, C = map(list, input().split())

    visited = [[False for _ in range(len(B)+1)]
               for _ in range(len(A)+1)]  # a, b를 넣기위해
    queue = deque()
    queue.append((0, 0))

    c = 0

    while queue:
        for _ in range(len(queue)):
            a, b = queue.popleft()

            if a < len(A) and not visited[a+1][b] and A[a] == C[c]:
                visited[a+1][b] = True
                queue.append((a+1, b))

            # 두경우 다 가능해서 elif가 아닌 if
            if b < len(B) and not visited[a][b+1] and B[b] == C[c]:
                visited[a][b+1] = True
                queue.append((a, b+1))

        c += 1

    if c == len(C)+1:
        print("Data set %d: yes" % (i+1))
    else:
        print("Data set %d: no" % (i+1))
