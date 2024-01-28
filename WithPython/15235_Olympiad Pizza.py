# 백준 15235 Olympiad Pizza 실5

# 몇명은 1개 이상을 받고 싶어함 -> 받고 다시 뒤에 줄서기

# 얼마나 오래 걸리는지 계산

from collections import deque

N = int(input())

queue = deque()

arr = list(map(int, input().split()))
answer = [0 for _ in range(N)]

for i in range(N):
    queue.append(i)

t = 0
while queue:
    t += 1
    q = queue.popleft()

    arr[q] -= 1

    if arr[q] > 0:
        queue.append(q)
    elif arr[q] == 0:
        answer[q] = t

print(*answer)
