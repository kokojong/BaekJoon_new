# 2230 수 고르기 골5

N, M = map(int, input().split())

# 차이가 M이상이면서 가장 작은 경우

arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

l = 0
r = 0

answer = []

while l <= r and r < N:
    result = arr[r] - arr[l]

    if result >= M:
        answer.append(result)
        l += 1
    else:
        r += 1

answer.sort()
print(answer[0])
