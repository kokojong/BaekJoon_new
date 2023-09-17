# 백준 14719 빗물 골5

H, W = map(int, input().split())

board = [[0 for _ in range(W)] for _ in range(H)]

answer = 0

# 3 0 1 4
line = list(map(int, input().split()))

for c in range(W):  # column
    l = line[c]
    for r in range(H-l, H):  # row
        board[r][c] = 1


def checkBottom(r, c):
    if r == H-1:
        return True
    else:
        return board[r+1][c]


def checkLeft(r, c):
    if c == 0:
        return False

    for cc in range(c-1, -1, -1):
        if board[r][cc] == 1:
            return True
    return False


def checkRight(r, c):
    if c == W-1:
        return False

    for cc in range(c+1, W):
        if board[r][cc] == 1:
            return True
    return False


# 맨 아랫줄 맨 왼쪽부터 체크!
for r in range(H-1, -1, -1):
    for c in range(0, W):
        # print("r, c", r, c)
        if board[r][c] == 0:
            # print(checkBottom(r, c), checkLeft(r, c), checkRight(r, c))
            if checkBottom(r, c) and checkLeft(r, c) and checkRight(r, c):
                # print("ddd", r, c)
                board[r][c] = 1
                answer += 1
# print(board)
print(answer)
