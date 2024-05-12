# 백준 11497 통나무 건너뛰기 실1
from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    answer = deque()

    for i in range(N):
        if i % 2 == 0:
            answer.appendleft(arr[i])
        else:
            answer.append(arr[i])

    answer.append(answer[0])

    result = 0
    for i in range(N):
        r = abs(answer[i+1] - answer[i])
        result = max(r, result)

    print(result)
