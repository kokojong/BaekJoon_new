# 백준 17281 야구 골4

from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())

board = [[]]  # r 이닝의 c 선수의 기록

# 1번 선수는 4번으로타자 고정

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

posibles = list(permutations(range(0, 9), 9))  # 0~8까지 해서 9명 줄세우기
# 가능한 선수들의 모든 경우

# print("board", board)

answer = 0

for posible in posibles:
    # for _ in range(1):
    # posible = (4, 5, 6, 0, 1, 2, 3, 7, 8)
    if posible[3] != 0:  # 4번 타자는 항상 선수1
        continue

    # print("posible", posible)  # 선수들의 순서

    inning = 1
    idx = 0  # 현재 출전 선수
    out = 0
    bases = deque([0, 0, 0])

    point = 0

    while inning <= N:

        # print(bases)

        result = board[inning][posible[idx]]

        # print(inning, "inning", idx, result, bases)

        if result == 0:
            out += 1

        elif result == 1:
            bases.appendleft(1)
            point += bases.pop()
        elif result == 2:
            bases.appendleft(1)
            bases.appendleft(0)
            for _ in range(2):
                point += bases.pop()
        elif result == 3:
            bases.appendleft(1)
            bases.appendleft(0)
            bases.appendleft(0)
            for _ in range(3):
                point += bases.pop()
        elif result == 4:
            bases.appendleft(1)
            point += sum(bases)
            bases = deque([0, 0, 0])

        idx += 1
        idx %= 9

        if out == 3:
            inning += 1
            out = 0
            bases = deque([0, 0, 0])

    # print("posible, point", posible, point)

    answer = max(point, answer)

print(answer)
