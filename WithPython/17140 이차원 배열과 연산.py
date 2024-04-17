# 백준 17140 이차원 배열과 연산

from collections import defaultdict

R, C, K = map(int, input().split())
R -= 1
C -= 1

board = []
for _ in range(3):
    row = list(map(int, input().split()))
    board.append(row)

# 배열의 row, column의 최대 크기 -> 얘에 맞게 변화함
RR = 3
CC = 3


def funcR():
    # R연산

    global board
    global RR
    global CC

    rows = []
    maxRowLen = 0
    for r in range(RR):  # 행 별로 새로운 배열 만들기
        dic = defaultdict(int)
        for rr in board[r]:
            if rr == 0:
                continue
            dic[rr] += 1  # 딕셔너리에 처리

        # dicList -> [수, 등장횟수]의 배열 -> 추후 정렬이 필요함
        dicList = []
        for (k, v) in dic.items():
            dicList.append([k, v])

        # 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한
        dicList.sort(key=lambda x: (x[1], x[0]))
        # print("dicList", dicList)
        newRow = []
        for d in dicList:
            newRow.append(d[0])
            newRow.append(d[1])
        # print("newRow", newRow)
        if len(newRow) > 100:  # 잘라주기
            newRow = newRow[:100]

        rows.append(newRow)
        maxRowLen = max(len(newRow), maxRowLen)

    CC = maxRowLen

    for i in range(RR):
        rows[i] = rows[i] + [0 for _ in range(CC - len(rows[i]))]

    # print("new rows", rows)

    board = rows


def funcC():
    # C연산

    global board
    global RR
    global CC

    columns = []
    maxColumnLen = 0

    for c in range(CC):
        dic = defaultdict(int)
        for r in range(RR):
            if board[r][c] == 0:
                continue
            dic[board[r][c]] += 1

        dicList = []
        for (k, v) in dic.items():
            dicList.append([k, v])
        dicList.sort(key=lambda x: (x[1], x[0]))

        newColumn = []
        for d in dicList:
            newColumn.append(d[0])
            newColumn.append(d[1])

        if len(newColumn) > 100:
            newColumn = newColumn[:100]

        columns.append(newColumn)
        maxColumnLen = max(len(newColumn), maxColumnLen)

    RR = maxColumnLen

    for i in range(CC):
        columns[i] = columns[i] + [0 for _ in range(RR - len(columns[i]))]

    # print("new columns", columns)

    board = [[0 for _ in range(CC)] for _ in range(RR)]
    for r in range(RR):
        for c in range(CC):
            board[r][c] = columns[c][r]


cnt = 0
while cnt <= 100:
    if len(board) > R and len(board[0]) > C:
        if board[R][C] == K:
            print(cnt)
            exit()

    if RR >= CC:
        funcR()
    else:
        funcC()

    cnt += 1

if cnt == 101:
    print(-1)
