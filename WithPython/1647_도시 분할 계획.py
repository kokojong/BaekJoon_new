# 백준 1647 도시 분할 계획 골4

N, M = map(int, input().split())

graph = []

roots = [i for i in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append([a, b, c])

graph.sort(key=lambda x: x[2])


def find(x):
    if x != roots[x]:
        roots[x] = find(roots[x])

    return roots[x]


def union(a, b):

    parentA = find(a)
    parentB = find(b)

    if parentA < parentB:
        roots[parentB] = parentA
    elif parentA > parentB:
        roots[parentB] = parentA


stack = []
answer = 0
for a, b, c in graph:
    if find(a) != find(b):
        union(a, b)
        stack.append(c)
        answer += c

answer -= stack.pop()  # 마지막에 넣은간선 제거(다 연결 안되게 되며 제일 가중치 높음)
print(answer)
