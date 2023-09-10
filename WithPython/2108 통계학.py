# 백준 2108 통계학 실3

from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

answer1 = round(sum(arr) / len(arr))
answer2 = arr[N//2]

answer4 = arr[-1] - arr[0]

cnt = Counter(arr).most_common(2)

if len(arr) > 1:
    if cnt[0][1] == cnt[1][1]:
        answer3 = cnt[1][0]
    else:
        answer3 = cnt[0][0]
else:
    answer3 = cnt[0][0]

print(answer1)
print(answer2)
print(answer3)
print(answer4)
