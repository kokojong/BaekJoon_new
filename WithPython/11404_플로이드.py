# 백준 11404 플로이드 골4

# 플로이드 와샬 알고리즘!!!!!!
# k i j 기억하기

n = int(input())  # 도시수
m = int(input())  # 간선 수

INF = float('inf')
board = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    board[start][end] = min(board[start][end], cost)


for k in range(1, n+1):  # 중간
    for i in range(1, n+1):  # 시작
        for j in range(1, n+1):  # 끝

            if i == j:
                continue

            if board[i][k] < INF and board[k][j] < INF:  # 둘다 연결이 된거면
                if board[i][j] == INF:  # i랑 J랑 연결이 안된거면
                    board[i][j] = board[i][k] + board[k][j]
                else:
                    board[i][j] = min(board[i][j], board[i][k] + board[k][j])


for r in range(1, n+1):
    row = []
    for c in range(1, n+1):
        if board[r][c] == INF:
            row.append(0)
        else:
            row.append(board[r][c])
    print(" ".join(map(str, row)))
