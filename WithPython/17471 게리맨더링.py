# 백준 17471 게리맨더링 골4

from collections import deque
import copy

N = int(input())

peoples = list(map(int, input().split()))  # 인구수

graph = [[] for _ in range(N+1)]

for i in range(N):
    connect = list(map(int, input().split()))[1:]

    for j in connect:
        graph[i].append(j-1)
        graph[j-1].append(i)

posibles = []

word = []


def backtrack():
    if len(word) == N:
        posibles.append(copy.deepcopy(word))
        return

    word.append(True)
    backtrack()
    word.pop()

    word.append(False)
    backtrack()
    word.pop()


backtrack()


def BFS(arr, x):  # 어디에 속해있는지 여부
    visited = [False for _ in range(N)]
    visited[x] = True

    queue = deque()
    queue.append(x)

    connected = 1  # 연결된 수
    total = 0  # 총합

    while queue:
        q = queue.popleft()
        total += peoples[q]

        for next in graph[q]:
            if not visited[next] and arr[next] == arr[x]:
                queue.append(next)
                visited[next] = True
                connected += 1

    # print("connected", connected, total)
    return connected, total


answer = float('inf')
for posible in posibles:  # 2^N
    Trues = []
    Falses = []

    c1, t1 = BFS(posible, 0)  # 0으로 부터 시작한거
    c2 = 0
    t2 = 0

    for i in range(1, N):
        if posible[i] != posible[0]:
            c2, t2 = BFS(posible, i)
            break  # 더이상 진행 x
    if c1 == N:
        continue

    if c1 + c2 == N:
        answer = min(abs(t1 - t2), answer)  # 둘의 차이가 최소인 것을 찾기

if answer == float('inf'):
    print(-1)
else:
    print(answer)
