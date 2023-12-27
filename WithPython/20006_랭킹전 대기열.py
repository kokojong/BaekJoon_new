# 백준 20006 랭킹전 대기열 실1

p, m = map(int, input().split())

rooms = []
# room: [[level, name]]

for _ in range(p):
    level, name = map(str, input().split())
    level = int(level)

    posible = False
    for i in range(len(rooms)):
        limit = rooms[i][0][0]

        # 입장 가능하면
        if abs(level - limit) <= 10 and len(rooms[i]) < m:
            rooms[i].append([level, name])
            posible = True
            break

    # 다 돌았는데도 없다면
    if not posible:
        newRoom = [[level, name]]
        rooms.append(newRoom)

for room in rooms:
    # print("room", room)
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")

    sortedRoom = sorted(room, key=lambda x: x[1])
    for person in sortedRoom:
        print(*person)
