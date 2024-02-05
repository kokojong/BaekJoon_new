# 백준 18428 감시 피하기 골5

# N*N 크기 복도
# 선생님, 학생, 장애물
# 선생님은 4방향으로 감시, 단 장애물 만나면 뒤에 감시 못함
# 장애물을 3개 설치해서 모든 학생이 감시를 피할수 있는지 체크

# N이 3~6 이기 떄문에 36C3 하는것은 시간복잡도 상 괜춘

from itertools import combinations

N = int(input())

board = []

teachers = []
spaces = []

for r in range(N):
    row = list(map(str, input().split()))
    board.append(row)

    for c in range(N):
        if row[c] == 'T':
            teachers.append((r, c))
        elif row[c] == 'X':
            spaces.append((r, c))
# print(board)
# print(teachers)


def checkBoard():
    for tr, tc in teachers:

        # 선생님 위치에서 감시
        for r in range(tr, -1, -1):
            if board[r][tc] == 'S':
                return False
            if board[r][tc] == 'O':
                break  # 만나면 멈추기

        for r in range(tr, N):
            if board[r][tc] == 'S':
                return False
            if board[r][tc] == 'O':
                break  # 만나면 멈추기

        for c in range(tc, -1, -1):
            # print("tr, tc, c", tr, tc, c)
            if board[tr][c] == 'S':
                return False
            if board[tr][c] == 'O':
                break  # 만나면 멈추기

        for c in range(tc, N):
            if board[tr][c] == 'S':
                return False
            if board[tr][c] == 'O':
                break  # 만나면 멈추기
    return True


for (r1, c1), (r2, c2), (r3, c3) in combinations(spaces, 3):
    board[r1][c1] = 'O'
    board[r2][c2] = 'O'
    board[r3][c3] = 'O'

    if checkBoard():
        print('YES')
        # print(r1, c1, r2, c2, r3, c3)
        exit()

    board[r1][c1] = 'X'
    board[r2][c2] = 'X'
    board[r3][c3] = 'X'

print('NO')

# 4
# X S X T
# X X S X
# X X X X
# T T T X

# 5
# X X S X X
# X X X X X
# S X T X S
# X X X X X
# X X S X X
