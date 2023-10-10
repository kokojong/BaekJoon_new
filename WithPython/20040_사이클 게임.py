# 백준 20040 사이클 게임 골4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parents = [i for i in range(N)]


def findParent(a):
    if a != parents[a]:
        parents[a] = findParent(parents[a])

    return parents[a]


for m in range(M):
    a, b = map(int, input().split())

    parentA = findParent(a)
    parentB = findParent(b)

    if parentA != parentB:
        if parentA < parentB:
            parents[parentB] = parentA
        else:
            parents[parentA] = parentB
    else:  # 사이클 생성
        print(m + 1)
        exit()

print(0)
