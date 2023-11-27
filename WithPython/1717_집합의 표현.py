# 백준 1717 집합의 표현 골5

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())

parents = [i for i in range(n+1)]


def findParent(x):
    if x != parents[x]:
        parents[x] = findParent(parents[x])

    return parents[x]


for _ in range(m):
    c, a, b = map(int, input().split())

    parentA = findParent(a)
    parentB = findParent(b)
    if c == 0:
        if parentA != parentB:
            if parentA < parentB:
                parents[parentB] = parentA
            else:
                parents[parentA] = parentB

    else:
        if parentA == parentB:
            print("YES")
        else:
            print("NO")
