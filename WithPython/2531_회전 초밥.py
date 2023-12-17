# 백준 2531 회전 초밥 실1

N, d, k, c = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(int(input()))

arr += arr[:k]

answer = 0

for i in range(0, N+k):  # 길이가 k인 연속 접시
    part = arr[i:i+k] + [c]  # 쿠폰은 무조건 가능
    p = len(set(part))
    answer = max(answer, p)

print(answer)
