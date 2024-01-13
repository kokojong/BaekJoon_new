# 백준 1515 수 이어쓰기 실3

import sys
input = sys.stdin.readline

arr = list(input().rstrip())

n = 0
idx = 0

while True:
    n += 1

    for s in str(n):
        if arr[idx] == s:
            idx += 1
            if idx == len(arr):
                print(n)
                exit()
