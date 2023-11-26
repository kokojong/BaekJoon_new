# 백준 13023 ABCDE 골5

N, M = map(int, input().split())  # 사람수, 친구관계수

graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0


def DFS(n, depth):  # n부터 시작하는 것 만들기
    if depth == 4:
        print(1)
        exit()

    for g in graph[n]:
        if visited[g]:
            continue
        visited[g] = True
        DFS(g, depth+1)
        visited[g] = False


for i in range(N):  # dfs
    visited[i] = True
    DFS(i, 0)
    visited[i] = False

print(0)
