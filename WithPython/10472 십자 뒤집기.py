# 백준 10472 십자 뒤집기 골5

board = []
for _ in range(3):
    row = []
    for a in list(input()):
        if a == "*":
            row.append(0)
        else:
            row.append(1)
    board.append(row)


target = []
for _ in range(3):
    row = []
    for a in list(input()):
        if a == "*":
            row.append(0)
        else:
            row.append(1)
    target.append(row)
