# 백준 2467 용액 골5

N = int(input())
arr = list(map(int, input().split()))

l = 0
r = len(arr) - 1

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
    elif result == 0:
        break
    else:
        r -= 1

print(left, right)
