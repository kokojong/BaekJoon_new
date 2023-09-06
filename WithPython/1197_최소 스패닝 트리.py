# 백준 1197 최소 스패닝 트리 골4

import sys
input = sys.stdin.readline


V, E = map(int, input().split())
roots = [i for i in range(V+1)]

graph = []

for e in range(E):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))


graph.sort(key=lambda x: x[2])  # 가중치가 제일 작은거 부터 연결

# print(graph)

def findRoot(x):
    if x != roots[x]:
        roots[x] = findRoot(roots[x])

    return roots[x]


answer = 0

for a, b, c in graph:
    rootA = findRoot(a)
    rootB = findRoot(b)

    if rootA != rootB:
        if rootA < rootB:
            roots[rootB] = rootA
        else:
            roots[rootA] = rootB

        answer += c

print(answer)
