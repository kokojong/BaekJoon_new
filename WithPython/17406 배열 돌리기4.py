# 백준 17406 배열 돌리기 4 골4

from itertools import permutations
import copy
from collections import deque

R, C, K = map(int, input().split())

board = []

for _ in range(R):
    row = list(map(int, input().split()))
    board.append(row)

turns = []

for _ in range(K):
    r, c, s = map(int, input().split())  # r, c 기준으로 좌우 길이가 s인만큼씩 돌리기
    turns.append((r-1, c-1, s))


def turn(board, r, c, s):
    # print("trun", board, r, c, s)
    for ss in range(1, s+1):
        # rr: r-ss ~ r+ss
        # cc: c-ss ~ c+ss

        target = deque()
        for cc in range(c-ss, c+ss):  # top
            target.append(board[r-ss][cc])

        for rr in range(r-ss, r+ss):  # right
            target.append(board[rr][c+ss])

        for cc in range(c+ss, c-ss, -1):  # bottom
            target.append(board[r+ss][cc])

        for rr in range(r+ss, r-ss, -1):  # left
            target.append(board[rr][c-ss])

        target.appendleft(target.pop())

        for cc in range(c-ss, c+ss):  # top
            board[r-ss][cc] = target.popleft()

        for rr in range(r-ss, r+ss):  # right
            board[rr][c+ss] = target.popleft()

        for cc in range(c+ss, c-ss, -1):  # bottom
            board[r+ss][cc] = target.popleft()

        for rr in range(r+ss, r-ss, -1):  # left
            board[rr][c-ss] = target.popleft()

    # print("돌아간거", board)


answer = 5000
for posible in permutations(range(0, K), K):
    # 가능한 배열

    newBoard = copy.deepcopy(board)

    # print("posible", posible)

    # posible -> 가능한 경우의 수

    for p in posible:
        turn(newBoard, turns[p][0], turns[p][1], turns[p][2])

    result = 5000
    for row in newBoard:
        result = min(sum(row), result)

    answer = min(result, answer)

print(answer)
# 5 6 1
# 1 2 3 2 5 6
# 3 8 7 2 1 3
# 8 2 3 1 4 5
# 3 4 5 1 1 1
# 9 3 2 1 4 3
# 4 2 1
