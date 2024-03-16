# 백준 2310 어드벤처 게임 골4

# 1~N번까지 번호가 붙은 방

# 해당하는 번호로 바로 이동, 방안에 레프리콘or트롤
# 레프리콘은 일정량 이하로 떨어지지 않게 채워줌.
# 트롤는 통행료 지불

# 1번방에서 출발해서 N번방에 도착이 가능한지?

def DFS(now, money):
    global visited
    global answer

    if answer:
        return

    cost = rooms[now][1]

    if rooms[now][0] == "L":
        if cost > money:
            money = cost

    if rooms[now][0] == "T":
        if cost > money:
            return  # 통과 못하는 경우
        else:
            money -= cost  # 돈 쓰기

    if now == N:
        answer = True
        return

    visited[now] = True
    for next in rooms[now][2]:
        if not visited[next]:
            DFS(next, money)
    visited[now] = False


while True:
    N = int(input())

    if N == 0:
        break

    visited = [False for _ in range(N+1)]
    money = 0

    rooms = [[]]

    answer = False

    for _ in range(N):
        tmp = input().split()
        # 타입, cost, 연결된 방 번호들
        rooms.append([tmp[0], int(tmp[1]), map(int, tmp[2:-1])])

    DFS(1, 0)

    if answer:
        print("Yes")
    else:
        print("No")
