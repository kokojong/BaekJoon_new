# 백준 4179 불!

from collections import deque

R, C = map(int, input().split())

board = []

visited_human = [[0] * C for _ in range(R)]
visited_fire = [[0] * C for _ in range(R)]

humanQueue = deque()
fireQueue = deque()

for r in range(R):
    row = list(input())
    board.append(row)
    for c in range(C):
        if row[c] == 'J':
            humanQueue.append([r, c])
            visited_human[r][c] = 1
        elif row[c] == 'F':
            fireQueue.append([r, c])
            visited_fire[r][c] = 1


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs():
    while fireQueue:
        fr, fc = fireQueue.popleft()

        for i in range(4):
            rr = fr + dr[i]
            cc = fc + dc[i]

            if 0 <= rr < R and 0 <= cc < C and board[rr][cc] != '#' and visited_fire[rr][cc] == 0:
                visited_fire[rr][cc] = visited_fire[fr][fc] + 1
                fireQueue.append([rr, cc])
    # print("visited_fire", visited_fire)
    while humanQueue:
        hr, hc = humanQueue.popleft()

        for j in range(4):
            rr = hr + dr[j]
            cc = hc + dc[j]

            if 0 <= rr < R and 0 <= cc < C:
                if board[rr][cc] != '#' and visited_human[rr][cc] == 0:
                    # 불이 안왔거나 내가 먼저옴
                    if visited_fire[rr][cc] == 0 or (visited_human[hr][hc] + 1 < visited_fire[rr][cc]):
                        visited_human[rr][cc] = visited_human[hr][hc] + 1
                        humanQueue.append([rr, cc])

            else:
                return visited_human[hr][hc]
        # print("visited_human", visited_human)
    return "IMPOSSIBLE"


print(bfs())
