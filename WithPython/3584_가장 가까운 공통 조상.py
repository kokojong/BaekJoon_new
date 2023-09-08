# 백준 3584 가장 가까운 공통 조상 골4

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

T = int(input())


def findParent(x, arr):
    arr.append(x)
    if parents[x] != x:
        parents[x] = findParent(parents[x], arr)

    return parents[x]


def findCommonParent(arrA, arrB):
    for a in arrA:
        for b in arrB:
            if a == b:
                return a


for _ in range(T):
    N = int(input())

    parents = [i for i in range(N+1)]  # 1이상 N이하의 정수이므로

    for _ in range(N-1):
        a, b = map(int, input().split())
        parents[b] = a

    A, B = map(int, input().split())

    parentsA = []
    parentsB = []
    findParent(A, parentsA)
    findParent(B, parentsB)

    print(findCommonParent(parentsA, parentsB))
