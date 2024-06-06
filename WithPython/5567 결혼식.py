# # 백준 5567 결혼식 실2

# N = int(input())
# M = int(input())

# parents = [i for i in range(N+1)]


# def findParents(x):
#     if parents[x] != x:
#         parents[x] = findParents(parents[x])

#     return parents[x]


# def union(A, B):
#     a = findParents(A)
#     b = findParents(B)

#     if a < b:
#         parents[b] = a

#     elif a > b:
#         parents[a] = b


# for _ in range(M):
#     A, B = map(int, input().split())
#     union(A, B)

# # print(parents)
# answer = 0
# for i in range(1, N+1):
#     if parents[i] == 1:
#         answer += 1

# if answer == 1:
#     print(0)
# else:
#     print(answer-1)

# 처음에는 union find를 하려고 했는데 정렬 상태에 따라 이게 달라질수 있다는걸 파악함. -> 실제로 실패
# 단순히 bfs로 수정

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(x):
    q = deque()
    visited[x] = 1
    q.append(x)
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[a] + 1


bfs(1)
result = 0
for i in range(2, n+1):
    # 본인이거나 친구거나, 친구의 친구거나 경우의 수가 최대 3개
    if visited[i] < 4 and visited[i] != 0:
        result += 1
print(result)
