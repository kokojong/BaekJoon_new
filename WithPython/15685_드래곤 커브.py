# 백준 15685 드래곤 커브 골3

import sys
input = sys.stdin.readline

N = int(input())


dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

# 네 꼭지점이 모두 드래곤 커브의 일부 -> r,c를 기준으로 4개가 모두 True이면 += 1
board = [[False for _ in range(101)] for _ in range(101)]


# 여기에서 r, c 의 순서로 적어서 틀렸었다... 나는 바보
def dragon(c, r, d, g):
    generation = 0
    directions = [d]  # 이동하는 방향을 저장
    board[r][c] = True

    while True:
        if generation == g:
            break
        generation += 1

        for n in reversed(directions):
            dir = (n+1) % 4
            directions.append(dir)

    # print(directions)
    for dd in directions:
        r = r + dr[dd]
        c = c + dc[dd]

        if 0 <= r <= 101 and 0 <= c <= 101:
            # print("r, c", r, c)
            board[r][c] = True


for _ in range(N):
    c, r, d, g = map(int, input().split())
    dragon(c, r, d, g)

# dragon(3, 3, 0, 1)
# dragon(4, 2, 1, 3)
# dragon(4, 2, 2, 1)


answer = 0
for i in range(100):
    for j in range(100):

        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            answer += 1
print(answer)
