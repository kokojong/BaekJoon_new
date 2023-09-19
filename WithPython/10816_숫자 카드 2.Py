# 백준 10816 숫자 카드 2 실4

from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
dic = defaultdict(int)
arr = list(map(int, input().split()))

for a in arr:
    dic[a] += 1

M = int(input())
inputs = list(map(int, input().split()))

answer = []
for i in inputs:
    answer.append(dic[i])

print(' '.join(map(str, answer)))
