# 26091 현대모비스 소프트웨어 아카데미 실1

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
# print(arr)

l = 0
r = N-1

answer = 0

while l < r and 0 <= l < N and 0 <= r < N:
    result = arr[l] + arr[r]

    if result >= M:  # 가능한거면
        l += 1
        r -= 1
        answer += 1

    else:
        l += 1

print(answer)
