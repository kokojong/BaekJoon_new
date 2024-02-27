# 백준 18353 병사 배치하기 실2

# 남아있는 애들이 내림차순이 되게하고 열외를 시킬수 있음
# 남은 병사 수가 최대가 되게 하려면 열외해야하는 병사의 수

N = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):  # i이전까지만 체크
        if arr[i] < arr[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(N - max(dp))
