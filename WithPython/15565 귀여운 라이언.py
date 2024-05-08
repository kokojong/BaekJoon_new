# 백준 15565 귀여운 라이언 실1

# 1이 K개 이상 있는 가장 작은 연속된 집합의 크기

N, K = map(int, input().split())

answer = float('inf')
arr = list(map(int, input().split()))

left = 0
right = 0

now = 0
if arr[0] == 1:
    now += 1

while left <= right and right < N and left < N:
    if now < K:
        right += 1
        if right < N and arr[right] == 1:
            now += 1

    elif now == K:
        answer = min(right - left + 1, answer)  # 길이
        left += 1
        if arr[left-1] == 1:
            now -= 1
        # print(left, right)
        # break

    else:
        left += 1
        if arr[left-1] == 1:
            now -= 1
if answer == float('inf'):
    print(-1)
else:
    print(answer)
