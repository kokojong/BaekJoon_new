# 백준 4811 알약 골5

# 반개 or 한개를 꺼내기 dp

dp = [[0 for _ in range(31)] for _ in range(31)]
# w, h

for h in range(1, 31):
    dp[0][h] = 1

for w in range(1, 31):
    for h in range(30):
        if h == 0:  # h가 없다면 무조건 w를 선택해야함
            dp[w][h] = dp[w-1][h+1]
        else:
            dp[w][h] = dp[w-1][h+1] + dp[w][h-1]
            # h가 1개 줄고 w가 1개 느는거(H동작) or h는 그대로 두고 w가 1개 주는거(W동작(

while True:
    N = int(input())
    if N == 0:
        break

    print(dp[N][0])  # W가 N개 있는거
