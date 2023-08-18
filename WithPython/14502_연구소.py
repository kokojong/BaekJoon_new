# 백준 14502 연구소 골4

# 이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳
# 벽은 3개를 딱 세워야함

# 세로 N 가로 M

# idea: 모든 빈칸의 배열을 만들고 3개를 뽑는 경우의 수(combination) 만들어서 뽑기
# 뽑은 경우로 벽을 세웠다고 가정하고 virus부터 dfs 하기(bfs도 될듯 -> 난 bfs해야지)
# 다 돌고나서 0으로 이어진 애들을 또 dfs로 돌면서 몇개가 연결되어 있는지 확인하고 최대 크기 return
# -> 이건 알고보니 연결된게 아니라 그냥 0의 갯수를 세어주는거였다 ㅎ... 어쩐지 너무 코드가 길어질것 같긴 했다.

from collections import deque
from itertools import combinations
import copy
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

board = []

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

viruses = []  # 바이러스의 배열
safe = []  # 빈 칸

for r in range(N):
    for c in range(M):
        if board[r][c] == 2:
            viruses.append([r, c])
        elif board[r][c] == 0:
            safe.append([r, c])

# print("virus", viruses)
# print("safe", safe)

posibles = list(combinations(safe, 3))


def bfs(q, board):
    queue = deque()
    queue.append(q)
    # print("queue", queue)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while queue:
        q = queue.popleft()
        r = q[0]
        c = q[1]

        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0 <= rr < N and 0 <= cc < M and board[rr][cc] == 0:  # 빈 공간일때만
                board[rr][cc] = 2  # 바이러스 감염
                queue.append([rr, cc])

    # print("result", board)

    return board


answer = []  # 연결된 안전지역의 최대 크기의 배열


def wall(posible, board):  # 3개를 뽑은 배열
    newBoard = copy.deepcopy(board)
    for p in posible:
        newBoard[p[0]][p[1]] = 1  # 벽을 세움

    for virus in viruses:
        result = bfs(virus, newBoard)  # 바이러스가 전파 되고 난 결과 board -> 전파된건 2로 갱신됨
        cnt = 0
        for r in range(N):
            for c in range(M):
                if result[r][c] == 0:
                    cnt += 1
    answer.append(cnt)


for posible in posibles:
    wall(posible, board)
# wall(posibles[0], board)

print(max(answer))
