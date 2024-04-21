# 백준 13265 색칠하기 골5

# 연결된 애들끼리 묶기 -> 얘네에서 2가지 색으로 색칠이 가능한지 체크
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

def BFS(x):
    global color

    queue = deque()
    queue.append(x)

    color[x] = 1

    while queue:
        q = queue.popleft()

        for next in graph[q]:
            if color[next] == 0:  # 아직 방문안한거면
                color[next] = -color[q]  # 부호 바꿔주기
                queue.append(next)
            elif color[next] == color[q]:  # 이미 같은게 있다면!
                return False

    return True


for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    color = [0 for _ in range(N+1)]  # visited처럼 체크하기

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    possible = True

    for i in range(1, N+1):
        if color[i] == 0:
            result = BFS(i)
            # print("i, result", i, result)
            if result == False:
                possible = False
                break

    if possible:
        print("possible")
    else:
        print("impossible")
