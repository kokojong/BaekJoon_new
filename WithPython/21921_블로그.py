# 백준 21921 블로그 실3

from collections import Counter

N, X = map(int, input().split())

arr = list(map(int, input().split()))

now = 0
for i in range(X):
    now += arr[i]

results = [now]

for i in range(1, N-X+1):
    now -= arr[i-1]
    now += arr[i+X-1]

    results.append(now)

results.sort(reverse=True)

if results[0] == 0:
    print('SAD')
else:
    print(results[0])
    print(Counter(results)[results[0]])
