# 백준 3190 뱀 골4

# idea: queue로 뱀을 만들기!!
# L D에 따라서 방향을 바꿔줘야 하니까 그전 방향 기억하기(U R L D) 이런식으로

from collections import deque
from collections import defaultdict

N = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

K = int(input())  # 사과의 수

for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1  # 1행 1열 -> 0,0

L = int(input())

lines = defaultdict(str)
for _ in range(L):
    X, C = map(str, input().split())  # X초에 C로 방향이 변경
    X = int(X)
    lines[X] = C
# print(lines)

snake = deque([[0, 0]])  # r, c
# C가 D이면 +1, L이면 -1 %4

time = 0
head = [0, 0]

d = 1  # 방향 저장 (U R D L - 0 1 2 3)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:  # 일단! lines 빼고 먼저 구현
    s = snake[-1]  # 가장 뒤에꺼
    time += 1

    r = s[0]
    c = s[1]
    rr = r + dr[d]
    cc = c + dc[d]
    # print(rr, cc, d, snake)

    if lines[time] == 'D':
        d = (d + 1 + 4) % 4
    elif lines[time] == 'L':
        d = (d - 1 + 4) % 4

    # 벽을 안만나고, snake를 안만났다면
    if 0 <= rr < N and 0 <= cc < N and [rr, cc] not in snake:
        if board[rr][cc] == 1:  # 사과를 먹으면 꼬리는 그대로 두고 머리만 +1
            board[rr][cc] = 0
            snake.append([rr, cc])
        else:
            snake.popleft()
            snake.append([rr, cc])

    else:
        # print("정지", [rr, cc])
        break

# print(snake)
print(time)
