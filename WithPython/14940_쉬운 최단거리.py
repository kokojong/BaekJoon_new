# 백준 14940 쉬운 최단거리 실1

from collections import deque
import sys
input = sys.stdin.readline


# n: 세로, m: 가로
# 0: 못감, 1: 갈수있음 2: 목표지점(2는 단 한개)

# 2에서부터 시작해서 bfs로 하고 끝나고도 도달하지 못하는 애는 -1 출력
# 처음에 1인애들을 그냥 -1로 만들기?

n, m = map(int, input().split())  # n과 m을 반대로 썼음.....

board = []

# answer = [[-1 for _ in range(m)] for _ in range(n)] # -1로 초기화 -

for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)
start = []
for r in range(n):
    for c in range(m):
        if board[r][c] == 1:
            board[r][c] = -1  # 도달못하는거 -1로 초기화 하려고 만듬
        elif board[r][c] == 2:
            start.append([r, c])  # 시작점

queue = deque(start)  # r, c
# print(queue)
# print(start)
board[start[0][0]][start[0][1]] = 0  # 시작점은 0만큼의 거리


def bfs():

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while queue:
        q = queue.popleft()
        r = q[0]
        c = q[1]

        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0 <= rr < n and 0 <= cc < m and board[rr][cc] == -1:
                board[rr][cc] = board[r][c] + 1
                queue.append([rr, cc])


bfs()

# print(board)
for row in board:
    for i in row:
        print(i, end=" ")
    print()
