# 백준 16139 인간-컴퓨터 상호작용 실1

from collections import defaultdict
import sys
input = sys.stdin.readline


S = list(input().rstrip())

# print(S)

arr = [[0 for _ in range(len(S))] for _ in range(26)]  # S개 만큼 누적합 해두기
# r -> 알파벳의 숫자, c -> 갯수

for i in range(len(S)):
    s = ord(S[i]) - ord('a')  # int형
    # print(S[i], s)
    if i > 0:
        for k in range(26):
            arr[k][i] = arr[k][i-1]
    arr[s][i] += 1

# print(arr)

Q = int(input())

for _ in range(Q):
    a, l, r = map(str, input().split())
    a = ord(a) - ord('a')
    l = int(l)
    r = int(r)
    # print(a, l, r)
    result = arr[a][r]
    left = 0
    if l > 0:
        left = arr[a][l-1]
    result -= left
    print(result)
