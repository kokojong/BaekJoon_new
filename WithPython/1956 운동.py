# 백준 1956 운동 골4

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a -> b로 가는데 c의 가중치

# idea : board를 만들어서 각각 위치에서 다른 위치까지 가는데 걸리는 최소를 구하고 반대로 올때도 구해보기?

INF = float('inf')

board = [[INF for _ in range(V+1)] for _ in range(V+1)]

for a in range(V+1):
    for b, c in graph[a]:
        board[a][b] = c

# print(board)

for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            board[i][j] = min(board[i][k] + board[k][j], board[i][j])

answer = INF
for i in range(1, V+1):
    answer = min(board[i][i], answer)

if answer != INF:
    print(answer)
else:
    print(-1)
