# 백준 1535 안녕 실2

# 1~N
# i번 사람에게 인사를 하면 체력을 잃고 기쁨을 얻음
# 최대의 기쁨이 되도록

N = int(input())
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(101)] for _ in range(N+1)]  # 체력별로 기록

for i in range(1, N+1):
    for j in range(1, 101):
        if L[i] <= j:  # 넣을 수 있을 떄
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i])
        else:  # 넣을 수 없을 때
            dp[i][j] = dp[i-1][j]

print(dp[N][99])  # 100만큼 되면 죽은(?)거라서
