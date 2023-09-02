# 백준 2667 단지번호 붙이기 실1

from collections import deque
import sys
input = sys.stdin.readline
# import

N = int(input())

board = []
answer = []

for _ in range(N):
    row = list(map(int, input().rstrip()))
    board.append(row)


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(r, c, k):
    global board
    # cnt = 1 # 해당 단지의 크기
    queue = deque()
    queue.append((r, c))  # r, c에 k라고 기입
    cnt = 0
    while queue:
        qr, qc = queue.pop()
        if board[qr][qc] != 1:
            continue
        board[qr][qc] = k
        cnt += 1

        for i in range(4):
            rr = qr + dr[i]
            cc = qc + dc[i]

            if 0 <= rr < N and 0 <= cc < N and board[rr][cc] == 1:
                queue.append((rr, cc))

    answer.append(cnt)


k = 1  # k는 2부터 시작하기(구분용) - 단지번호
for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            k += 1
            bfs(r, c, k)
print(k-1)  # k-1개의 단지가 있다
# print(board)

answer.sort()
for a in answer:
    print(a)
