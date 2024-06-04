# 백준 2096 내려가기 골5

# import sys
# input = sys.stdin.readline

# N = int(input())

# arr = []

# for _ in range(N):
#     row = list(map(int, input().split()))
#     arr.append(row)

# minDP = [[0 for _ in range(3)] for _ in range(N)]
# maxDP = [[0 for _ in range(3)] for _ in range(N)]
# minDP[0] = arr[0]
# maxDP[0] = arr[0]

# for i in range(1, N):
#     minDP[i][0] = min(minDP[i-1][0], minDP[i-1][1]) + arr[i][0]
#     minDP[i][1] = min(minDP[i-1][0], minDP[i-1][1], minDP[i-1][2]) + arr[i][1]
#     minDP[i][2] = min(minDP[i-1][1], minDP[i-1][2]) + arr[i][2]

#     maxDP[i][0] = max(maxDP[i-1][0], maxDP[i-1][1]) + arr[i][0]
#     maxDP[i][1] = max(maxDP[i-1][0], maxDP[i-1][1], maxDP[i-1][2]) + arr[i][1]
#     maxDP[i][2] = max(maxDP[i-1][1], maxDP[i-1][2]) + arr[i][2]

# # print(maxDP)
# # print(minDP)
# print(max(maxDP[-1]), min(minDP[-1]))

# 위의 방법은 메모리 초과
from sys import stdin

N = int(input())
arr = list(map(int, stdin.readline().split()))
maxDP = arr
minDP = arr
for _ in range(N-1):
    arr = list(map(int, stdin.readline().split()))
    maxDP = [arr[0] + max(maxDP[0], maxDP[1]), arr[1] +
             max(maxDP), arr[2] + max(maxDP[1], maxDP[2])]
    minDP = [arr[0] + min(minDP[0], minDP[1]), arr[1] +
             min(minDP), arr[2] + min(minDP[1], minDP[2])]

print(max(maxDP), min(minDP))
