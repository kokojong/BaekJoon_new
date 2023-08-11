# 백준 1389 케빈 베이컨의 6단계 법칙 실1

from collections import deque

N, M = map(int, input().split(' '))

# 1부터 N+1 까지 직접 bfs로 걸리는 시간을 각각 구함

arr = [[] for _ in range(N+1)]  # 각 자리에서 직접 연결된 것의 모임

for m in range(M):
    a, b = map(int, input().split(' '))
    arr[a].append(b)
    arr[b].append(a)

answer = []


def bfs(k):
    distance = [0 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    visited[k] = True

    queue = deque(zip(arr[k], [1]*(N+1)))
    while queue:
        q, dis = queue.popleft()
        if visited[q] == False:
            visited[q] = True
            distance[q] = dis

            for a in arr[q]:
                queue.append((a, dis + 1))

    return sum(distance)  # k에서부터 걸리는 거리 총합


for i in range(1, N+1):
    answer.append(bfs(i))

minV = min(answer)
for v in enumerate(answer):
    if v[1] == minV:
        print(v[0]+1)
        break
