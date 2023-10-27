# 백준 4803 트리 골4

import sys
input = sys.stdin.readline
# Union find로도 풀 수 있음!


def DFS(parent, now):
    visited[now] = True

    for i in graphs[now]:
        if i == parent:
            continue

        if visited[i]:
            return False

        if not DFS(now, i):
            return False

    return True


c = 0
answer = 0
while True:
    c += 1
    answer = 0

    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break

    graphs = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())

        graphs[a].append(b)
        graphs[b].append(a)

    for i in range(1, N+1):
        if visited[i]:
            continue

        if DFS(0, i):
            answer += 1  # 트리수

    if answer == 0:
        print("Case {}: No trees.".format(c))
    elif answer == 1:
        print("Case {}: There is one tree.".format(c))
    else:
        print("Case {}: A forest of {} trees.".format(c, answer))
