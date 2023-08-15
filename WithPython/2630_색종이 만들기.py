# 백준 2630 색종이 만들기 실2

N = int(input())

board = []

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

white = 0  # 0
blue = 0  # 1

# idea: N을 반씩 나눠가면서 성공한건 -1로 바꾸자


def divide(row, column, n):
    global white
    global blue
    now = board[row][column]  # 무슨색인지
    isSame = True
    for r in range(row, row + n):
        for c in range(column, column + n):
            if board[r][c] != now or board[r][c] == -1:
                isSame = False
                break

    if isSame:
        if now == 1:
            blue += 1
        elif now == 0:
            white += 1

        for r in range(row, row + n):
            for c in range(column, column + n):
                board[r][c] = -1
    else:
        k = n//2  # 실수한 부분: k = N//2로 표기함..
        divide(row, column, k)
        divide(row + k, column, k)
        divide(row, column + k, k)
        divide(row + k, column + k, k)


divide(0, 0, N)

print(white)
print(blue)
