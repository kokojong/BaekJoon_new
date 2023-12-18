# 백준 2493 탑 골5

# 왼쪽으로 레이저 발사, 기둥 모두에 수신기
# 가장 먼저 만나는 탑에서만 수신이 가능

# 나보다 왼쪽에서 나보다 큰애를 만나야함..! (문제 조건에 모든 탑 높이 다름)

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

answer = []

stack = []  # index, value

for i in range(N):
    while stack:
        if arr[i] < stack[-1][1]:
            answer.append(stack[-1][0] + 1)  # ~번째
            break
        else:
            stack.pop()

    if not stack:
        answer.append(0)

    stack.append([i, arr[i]])

print(' '.join(map(str, answer)))
