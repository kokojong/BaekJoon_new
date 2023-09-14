# 백준 2470 두 용액 골5

import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
# print(arr)

arr.sort()

l = 0
r = N-1

left = arr[l]
right = arr[r]
now = abs(left + right)
while l < r:
    result = arr[l] + arr[r]

    if abs(result) < now:
        now = abs(result)
        left = arr[l]
        right = arr[r]

    if result < 0:
        l += 1
    elif result > 0:
        r -= 1
    else:  # 0이라면
        break

print(left, right)
