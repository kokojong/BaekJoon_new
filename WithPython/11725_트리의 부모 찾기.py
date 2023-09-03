# 백준 11725 트리의 부모 찾기 실2

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

# board = [[False for _ in range(N+1)] for _ in range(N+1)] # 연결되었는지
# 위와 같이 풀게되면 10만 * 10만의 배열이 필요해짐 -> 필요한 애들만 보기
graph = [[] for _ in range(N+1)]

parents = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])  # node, depth
while queue:
    node = queue.popleft()
    for g in graph[node]:  # 연결된 애들
        if parents[g] == 0:
            parents[g] = node
            queue.append(g)

for i in range(2, N+1):
    print(parents[i])
