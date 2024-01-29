# 백준 13604 전략 게임 브2

j, r = map(int, input().split())

arr = list(map(int, input().split()))

scores = [0 for _ in range(j)]

for i in range(j*r):
    scores[i % j] += arr[i]

result = max(scores)
for i in range(j):
    if scores[i] == result:
        answer = i+1

print(answer)
