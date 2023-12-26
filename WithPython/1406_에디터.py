# 백준 1406 에디터 실2

import sys
input = sys.stdin.readline

arr = list(input().rstrip())

N = len(arr)

M = int(input())

# left cursor right 요런식으로 표현
# right는 뒤집어진 stack으로 표현 - 가장 끝이 stack의 밑
left = arr
right = []

for _ in range(M):
    inputs = input().split()
    command = inputs[0]

    if command == "L":
        if left:
            right.append(left.pop())
    elif command == "D":
        if right:
            left.append(right.pop())
    elif command == "B":
        if left:
            left.pop()
    elif command == "P":
        s = inputs[1]
        left.append(s)

answer = left

while right:
    answer.append(right.pop())

print(''.join(answer))
