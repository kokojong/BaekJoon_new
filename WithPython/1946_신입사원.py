# 백준 1946 신입사원 실1

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    answer = N
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort(key=lambda x: x[0])

    lowest = arr[0][1]
    for i in range(1, N):
        if arr[i][1] > lowest:
            answer -= 1
        else:
            lowest = arr[i][1]

    print(answer)
