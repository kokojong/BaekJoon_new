# 백준 15591 MooTube 골5

# 각 애들끼리의 USADO가 주어지는데
# 각 동영상이 다른 애들과의 USADO를 봤을 때 K 이상이라면 추천되게
# 너무 많으면 안되니까 K를 적절히

from collections import deque

N, Q = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())  # a와 b가 c의 cost로 연결이 되어있음
    graph[a].append((b, c))
    graph[b].append((a, c))


def BFS(k, v):  # v에서 시작
    visited = [False for _ in range(N+1)]

    queue = deque()
    queue.append(v)
    visited[v] = True

    cnt = 0

    while queue:
        q = queue.popleft()

        for next, next_cost in graph[q]:
            if not visited[next]:
                if next_cost >= k:
                    visited[next] = True
                    queue.append(next)
                    cnt += 1

    return cnt


for _ in range(Q):
    k, v = map(int, input().split())

    print(BFS(k, v))
