# 백준 9205 맥주 마시며 이동하기 골5

# 맥주는 20개, 50m 갈때마다 마셔줘야함
# 편의점에서 빈병을 버리고 새 맥주로 구매가능, 편의점 떠날때도 1개 먹고 시작
# 거리 - x좌표 차이 + y좌표 차이
# 도착이 가능한지 체크

from collections import deque
T = int(input())


def BFS():
    queue = deque()
    queue.append(home)

    while queue:
        x, y = queue.popleft()

        if abs(x-rock[0]) + abs(y-rock[1]) <= 1000:
            print("happy")
            return

        for i in range(N):
            if not visited[i]:
                xx, yy = convinience[i]

                if abs(x-xx) + abs(y-yy) <= 1000:
                    queue.append([xx, yy])
                    visited[i] = True

    print("sad")
    return


for _ in range(T):
    N = int(input())
    home = list(map(int, input().split()))
    convinience = []
    for _ in range(N):
        cov = list(map(int, input().split()))
        convinience.append(cov)
    rock = list(map(int, input().split()))

    visited = [False for _ in range(N+1)]  # N개의 편의점
    BFS()
