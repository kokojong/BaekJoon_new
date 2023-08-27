# 백준 2293 동전1 골5

n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

coins.sort()

dp = [0 for _ in range(k+1)]
# dp[0] = 1  # dp 연산을 위해서 dp[0]은 1로 초기화 -> 이유: c == coin일때 dp[c-coin]을 하게되면 dp[0]이 되어서 0개로 세어지면 안된다

coin = coins[0]  # 가장 작은 코인으로 미리 초기화
for c in range(1, k+1):
    if c >= coin and c % coin == 0:  # 실수한 부분: 나눠지지 않는 경우도 존재
        dp[c] = 1

if n == 1:
    print(dp[k])
    exit()

for r in range(2, n+1):
    coin = coins[r-1]  # 새로운 동전 등장
    for c in range(1, k+1):
        # dp[c] - c를 표현 하는 방법의 수
        if c >= coin:  # 새로운 coin을 사용할 수 있다면
            dp[c] += dp[c-coin]  # 이제부터 2를 쓸 수 있게 된다면 2를 뺀 위치의 dp 만큼을 더해주기
# print(dp)
print(dp[k])
