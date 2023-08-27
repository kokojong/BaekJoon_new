# 백준 2294 동전2 골5

n, k = map(int, input().split())

dp = [10001 for _ in range(k+1)]
# 불가능한 경우 때문에 -1로 시작
dp[0] = 0

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()

for coin in coins:
    for i in range(1, k+1):
        if i >= coin:
            # 이전에 사용하던대로 하느냐 vs 새로운 동전을 사용하느냐
            dp[i] = min(dp[i], dp[i-coin] + 1)
            # 새로운 동전을 사용하면 해당 동전 크기만큼의 전 사용값 + 1(새 동전 사용)
            # ex) 1 5 12 순서대로 사용하는데
            # 15를 표현하려면 1, 5로 15를 표현했을때 vs (15-12)의 값 + 1(12를 사용)
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
