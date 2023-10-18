# 백준 1005 ACM Craft 골3

# 각각의 먼저 지어져야할 건물의 배열을 가지고 있고 암것도 없다면 성공 지을수 있는식으로 구현

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())  # 건물의 갯수 N, 건설 순서 규칙 총 갯수 K
    graph = [[] for _ in range(N+1)]  # 내가 건설되어야 진행할 수 있는 그래프(상위 건물)
    times = [0] + list(map(int, input().split()))  # 걸리는 시간
    degree = [0 for _ in range(N+1)]  # 진입 차수
    results = [0 for _ in range(N+1)]

    for _ in range(K):
        a, b = map(int, input().split())  # a 다음에 b가 지어져야함
        graph[a].append(b)
        degree[b] += 1

    W = int(input())

    queue = deque()

    for i in range(1, N+1):
        if degree[i] == 0:
            queue.append(i)
            results[i] = times[i]

    while queue:
        q = queue.popleft()

        for i in graph[q]:  # 뽑은애가 지어지고 지을 수 있는 건물 목록
            degree[i] -= 1
            results[i] = max(results[i], results[q] +
                             times[i])  # 이전위치 시간 + 걸리는 시간 dp

            if degree[i] == 0:
                queue.append(i)

    print(results[W])
