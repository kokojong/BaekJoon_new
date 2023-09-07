# 백준 2002 추월 실1

import sys
input = sys.stdin.readline

N = int(input())

stack = []  # 들어갈때의 순서대로 넣기
for _ in range(N):
    stack.append(str(input()).rstrip())

arr = []
for _ in range(N):
    arr.append(str(input()).rstrip())

answer = 0
passed = set()  # 이미 추워해버린 친구들
while stack:
    s = stack.pop()
    # print(s, arr, passed)

    while arr[-1] in passed:
        arr.pop()

    if s == arr[-1]:  # 추월하지 않았다면
        arr.pop()
    else:  # 추월했다면
        passed.add(s)
        answer += 1

print(answer)
