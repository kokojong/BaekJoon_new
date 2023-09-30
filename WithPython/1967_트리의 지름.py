# 백준 1967 트리의 지름 골4

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, c, cost = map(int, input().split())
    tree[p].append((c, cost))
    tree[c].append((p, cost))

distance = [-1 for _ in range(N+1)]
distance[1] = 0


def DFS(start, cost):
    for end, k in tree[start]:
        if distance[end] == -1:
            distance[end] = cost + k
            DFS(end, cost + k)

# 가장 먼 노드가 있다면 그것은 무조건 지름중에 하나


DFS(1, 0)
# print(distance)

index = 0
tmp = 0

for idx, dis in enumerate(distance):
    if dis > tmp:
        tmp = dis
        index = idx

distance = [-1 for _ in range(N+1)]
distance[index] = 0
DFS(index, 0)

print(max(distance))
