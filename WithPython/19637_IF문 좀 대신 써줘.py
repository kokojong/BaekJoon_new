# 백준 19637 IF문 좀 대신 써줘 실3

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

chings = []

for _ in range(N):
    name, numstr = map(str, input().split())
    num = int(numstr)
    chings.append((num, name))

# chings.sort()

# print("chings", chings)

for _ in range(M):
    m = int(input())
    l = 0
    r = N

    result = 0
    while l <= r:
        mid = (l+r)//2
        if chings[mid][0] >= m:
            result = mid
            r = mid - 1
        else:
            l = mid + 1
    print(chings[result][1])
