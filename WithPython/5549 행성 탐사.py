# 백준 5549 행성 탐사 골5

R, C = map(int, input().split())
K = int(input())

board = []
for _ in range(R):
    row = list(input())
    board.append(row)

# print(board)

jungles = [[0 for _ in range(C+1)] for _ in range(R+1)]
oceans = [[0 for _ in range(C+1)] for _ in range(R+1)]
ices = [[0 for _ in range(C+1)] for _ in range(R+1)]

for r in range(1, R+1):
    for c in range(1, C+1):
        jungles[r][c] = jungles[r][c-1]
        oceans[r][c] = oceans[r][c-1]
        ices[r][c] = ices[r][c-1]

        if board[r-1][c-1] == 'J':
            jungles[r][c] += 1

        if board[r-1][c-1] == 'O':
            oceans[r][c] += 1

        if board[r-1][c-1] == 'I':
            ices[r][c] += 1

# print(jungles)
# print(oceans)
# print(ices)

for _ in range(K):
    r1, c1, r2, c2 = map(int, input().split())

    j = 0
    o = 0
    i = 0

    j =
