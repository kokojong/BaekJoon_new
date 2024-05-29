# 백준 31589 포도주 시음 실3

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = 0

for i in range(N-1, N - (K+1)//2 - 1, -1):  # 뒤에서부터
    answer += arr[i]

for i in range(0, (K-1)//2):
    answer -= arr[i]

print(answer)
