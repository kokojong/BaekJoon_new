# 백준 7682 틱택토 골5

def checkArr(arr):
    cntX = arr.count('X')

    cntO = arr.count('O')

    cntComma = arr.count('.')

    if cntO > cntX or cntX - cntO > 1:
        return False

    board = []
    for i in range(3):
        board.append(arr[3*i:3*i+3])

    isXwin = False
    isOwin = False

    # 가로
    for i in range(3):
        row = ''.join(board[i])

        if row == "XXX":
            isXwin = True
        elif row == 'OOO':
            isOwin = True

    # 세로
    for j in range(3):
        tmp = []
        for i in range(3):
            tmp.append(board[i][j])
        column = ''.join(tmp)

        if column == "XXX":
            isXwin = True
        elif column == 'OOO':
            isOwin = True

    # 대각
    cross = []
    for i in range(3):
        # print("대각1", i, board[i][2-i])
        cross.append(board[i][i])
    c = ''.join(cross)

    if c == "XXX":
        isXwin = True
    elif c == 'OOO':
        isOwin = True

    # 대각2
    cross2 = []
    for i in range(3):
        cross2.append(board[i][2-i])

    c2 = ''.join(cross2)

    if c2 == "XXX":
        isXwin = True
    elif c2 == 'OOO':
        isOwin = True

    # print("isXwin", "isOwin", isXwin, isOwin)

    if isXwin and not isOwin:
        return True
    elif not isXwin and not isOwin:  # 무승부
        return True
    elif not isXwin and isOwin and cntO == cntX:
        return True
    else:
        return False


while True:
    line = input()
    if line == 'end':
        break
    arr = list(line)

    if checkArr(arr):
        print("valid")
    else:
        print("invalid")
