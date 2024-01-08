# 백준 20310 타노스 실3

from collections import Counter
import sys
input = sys.stdin.readline

arr = list(map(int, input().rstrip()))
counter = Counter(arr)
l = len(arr)

z = counter[0]//2
o = counter[1]//2

answer = []

for i in range(l):
    if arr[i] == 0:
        if z > 0:
            answer.append(0)
            z -= 1
        else:
            continue
    else:
        if o > 0:
            o -= 1
            continue
        else:
            answer.append(1)

print(''.join(map(str, answer)))

# 000011
