# 백준 1058 친구 실2

import sys
input = sys.stdin.readline

N = int(input())
friends = [list(input()) for _ in range(N)]

graph = [[False for _ in range(N)] for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            if friends[i][j] == "Y" or (friends[i][k] == "Y" and friends[k][j] == "Y"):
                graph[i][j] = True

answer = 0

for g in graph:
    answer = max(answer, sum(g))
print(answer)
