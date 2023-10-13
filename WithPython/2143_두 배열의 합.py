from collections import Counter
import sys
input = sys.stdin.readline


T = int(input())

n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

sums1 = [0]

tmp = 0
for a in arr1:
    tmp += a
    sums1.append(tmp)


sums2 = [0]
tmp = 0
for a in arr2:
    tmp += a
    sums2.append(tmp)
# i번부터 시작해서 길이 l의 누적합 -> sums[i] - sums[i-l]

A = []
for i in range(1, n+1):
    for j in range(i, n+1):
        total = sums1[j] - sums1[i-1]
        # print("i, j", i, j)
        A.append(total)

B = []
for i in range(1, m+1):
    for j in range(i, m+1):
        total = sums2[j] - sums2[i-1]
        # print("i, j", i, j)
        B.append(total)

A = Counter(A)
B = Counter(B)

answer = 0
for k, v in A.items():
    result = v * (B[T-k])
    answer += result

print(answer)
