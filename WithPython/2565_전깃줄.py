# 백준 2565 전깃줄 골5

# A -> B 로 되는데 A를 기준으로 오름차순 정렬

lines = []

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    lines.append([a, b])

lines.sort(key=lambda x: x[0])  # A기준 정렬

dp = [1 for _ in range(N)]  # B입장에서 A의 가장 긴 증가 수열 -> 교차되지 않는 가장 긴 수열

for i in range(1, N):
    for j in range(0, i):  # 이전 전선 확인
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
# print(dp)
print(N - max(dp))
