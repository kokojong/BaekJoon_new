# 백준 2346 풍선 터뜨리기 실3

from collections import deque

N = int(input())
queue = deque(list(enumerate(map(int, input().split()))))

answer = []

while queue:
    idx, value = queue.popleft()
    answer.append(idx + 1)

    if value > 0:
        queue.rotate(-(value - 1))  # value - 1 만큼 왼쪽으로 회전
    else:
        queue.rotate(-value)

print(''.join(map(str, answer)))
