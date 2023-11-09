# 백준 1253 좋다 골4

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

answer = 0

for i in range(N):
    num = arr[i]

    newArr = arr[:i] + arr[i+1:]

    l = 0
    # r = i-1 # 최적화를 위해 이렇게 했는데 음수가 있는걸 놓쳤다
    r = N-1 - 1
    # print(newArr)
    while l < r:
        tmp = newArr[l] + newArr[r]

        if tmp == num:
            answer += 1
            break

        if tmp < num:
            l += 1
        else:
            r -= 1

print(answer)
