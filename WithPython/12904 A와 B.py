# 백준 12904 A와 B 골5

# 문자열 뒤에 A추가
# 문자열 뒤집고 B추가

from collections import deque
import sys

input = sys.stdin.readline

r = False  # 뒤집힌 상태인지

arr1 = list(input().rstrip())
arr2 = deque(input().rstrip())

# print(arr1)
# print(arr2)

while True:
    if len(arr2) == len(arr1):
        break

    if r:
        if arr2[0] == 'A':
            arr2.popleft()
        else:
            arr2.popleft()
            r = False  # 다시 돌리기

    else:
        if arr2[-1] == 'A':
            arr2.pop()
        else:
            arr2.pop()
            r = True

    # print(arr2, r)

arr2 = list(arr2)
if r:
    arr2.reverse()
    if arr1 == arr2:
        print(1)
    else:
        print(0)
else:
    if arr1 == arr2:
        print(1)
    else:
        print(0)
