# 백준 1167 트리의 지름 골2

from collections import deque
import sys
input = sys.stdin.readline


V = int(input())

graph = [[] for _ in range(V+1)]  # 1~V

for v in range(V):
    li = list(map(int, input().split()))
    l = len(li)
    start = li[0]

    for i in range(1, l-1, 2):
        end, cost = li[i], li[i+1]
        graph[start].append([end, cost])


def bfs(start):

    visited = [-1 for _ in range(V+1)]
    queue = deque()
    queue.append(start)
    visited[start] = 0
    end = 0
    cost = 0

    while queue:
        q = queue.popleft()

        for e, c in graph[q]:
            if visited[e] == -1:
                visited[e] = visited[q] + c
                queue.append(e)
                if visited[e] > cost:
                    cost = visited[e]
                    end = e

    return (end, cost)


e, c = bfs(1)
answer = bfs(e)[1]  # cost
print(answer)

# 중요한 포인트는 모든 점을 다 보는게 아니라 아무점에서 탐색을 하고나면 그 결과에서 bfs를 한 제일 먼 거리가 무조건~ 지름!
# 2-1-3-4-5-6-7 이렇게 되어있다면 1에서 탐색을 하면 7이 선택되고 얘는 가장 먼 둘중에 하나일 수 밖에없음.
# 그래서 7에서 다시 탐색을 해주면 지름!
