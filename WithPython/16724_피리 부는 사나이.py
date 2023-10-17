# 백준 16724 피리 부는 사나이 골3

import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 행, 열

# 종착지점이 될 수 있는 곳을 고르고 그중에서 선택하기

# 아무지점에서 시작해서 따라가면서 그 사이클? 을 찾는다. 그 사이클의 갯수를 센다 -> 그럼 달성~

board = []

for _ in range(N):
    row = list(input().rstrip())
    board.append(row)

# print(board)

parents = [i for i in range(N*M)]


def move(r, c):
    dir = board[r][c]
    rr = r
    cc = c
    if dir == "U":
        rr = r - 1
    elif dir == "D":
        rr = r + 1
    elif dir == "R":
        cc = c + 1
    elif dir == "L":
        cc = c - 1

    # union
    parentA = findParent(r, c)
    parentB = findParent(rr, cc)

    # print("parentA, parentB", parentA, parentB)
    if parentA == parentB:
        return

    if parentA < parentB:
        parents[parentB] = parentA
    else:
        parents[parentA] = parentB
    # print("222 parentA, parentB", parentA, parentB, parents)
    move(rr, cc)


def findParent(r, c):
    if parents[r*M + c] != (r*M + c):
        parents[r*M + c] = findParent(parents[r*M + c] //
                                      M, parents[r*M + c] % M)

    return parents[r*M + c]


# 무조건적으로 다시 돌아오는 사이클이 아니기 때문에 다시 생각해줘야함
# cycle = 1
# for r in range(N):
#     for c in range(M):
#         if visited[r][c] > 0:
#             continue
#         visited[r][c] = cycle
#         move(r, c)
#         cycle += 1

# print(cycle - 1)

for r in range(N):
    for c in range(M):
        move(r, c)

print(len(set(parents)))

# 1 3
# RRL

# 정답: 1
# 출력: 0

# 10 10
# DRDRRRRRRD
# RDRUDUUUUL
# URLDLRRRRD
# RRRRLRDLUD
# DDRLLDULUU
# DRULLLRDUU
# DULLDDDURU
# URLDDDDUUL
# DLRLRDUULL
# RRULRUUURU

# 정답: 12
# 출력: 1
