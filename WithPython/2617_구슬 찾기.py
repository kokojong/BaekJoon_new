# 백준 2617 구슬 찾기 골4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

bigger = [[] for _ in range(N+1)]  # 나보다 큰 애들
smaller = [[] for _ in range(N+1)]  # 나보다 작은 애들

for _ in range(M):
    a, b = map(int, input().split())
    bigger[b].append(a)
    smaller[a].append(b)


def DFS(arr, start, visited):
    global cnt

    for a in arr[start]:
        if not visited[a]:
            visited[a] = True
            cnt += 1
            DFS(arr, a, visited)


answer = 0

for i in range(1, N+1):
    # visited = [False for _ in range(N+1)]

    cnt = 0  # 이어진 구슬?의 갯수
    DFS(bigger, i, [False for _ in range(N+1)])
    if cnt >= (N+1)/2:  # 이어진 구슬의 갯수가 중간값보다 멀리간다면(
        answer += 1

    cnt = 0
    DFS(smaller, i, [False for _ in range(N+1)])
    if cnt >= (N+1)/2:
        answer += 1

print(answer)
