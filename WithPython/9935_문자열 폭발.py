# 백준 9935 문자열 폭발 골4

import sys
input = sys.stdin.readline

s = list(input().rstrip())

target = list(input().rstrip())
t = len(target)


def checkWord():
    for j in range(-1, -t-1, -1):
        if stack[j] != target[j]:
            return False
    return True


stack = []
for i in range(len(s)):
    stack.append(s[i])
    # print(stack)
    if len(stack) >= t and checkWord():
        for _ in range(t):
            stack.pop()

if stack:
    print(''.join(map(str, stack)))
else:
    print("FRULA")
