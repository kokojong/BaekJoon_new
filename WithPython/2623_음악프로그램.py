# 백준 2623 음악프로그램 골3

from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())  # 가수의 수, pd의 수

# pd가 담당한 가수의 수, 그 만큼 가수들이 나옴

# 출연 순서 한줄씩 프린트, 만약 불가능하다면 0 출력

graph = [[] for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]

for _ in range(M):
    line = list(map(int, input().split()))
    for i in range(line[0] - 1):
        a = line[i+1]
        b = line[i+2]

        graph[a].append(b)  # a 다음에 해야할게 b
        degrees[b] += 1


queue = deque()
for i in range(1, N+1):
    if degrees[i] == 0:
        queue.append(i)

answer = []  # 완료한거

while queue:
    # print("queue", queue)
    q = queue.popleft()

    answer.append(q)

    for i in graph[q]:  # q가 선행되어야 하는 애들
        degrees[i] -= 1  # 앞에 없어졌으니까

        if degrees[i] == 0:
            queue.append(i)

if len(answer) == N:
    for a in answer:
        print(a)
else:
    print(0)
