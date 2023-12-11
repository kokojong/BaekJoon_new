# 백준 2688 줄어들지 않아 실1

# 1자리 -> 0 1 ... 9 (10개)
# 2자리 -> 00 01 ... 09 , 11 12...19, 99  10 + 9 + 8 .... 1 = 55
# 3자리 -> 000

# dp에 k 로 시작하는 갯수를 저장해두기?
# [1, 1, 1 ,... 1] 10개
# [10, 9, 8 ... 1] 55개
# [55, 55-10, 55-10-9 ... 1] 220개

dp = [[1 for _ in range(10)] for _ in range(65)]
sums = [0, 10]

for i in range(2, 65):
    dp[i][0] = sums[i-1]
    for j in range(1, 10):
        dp[i][j] = dp[i][j-1] - dp[i-1][j-1]
    sums.append(sum(dp[i]))

T = int(input())

for _ in range(T):
    n = int(input())  # n <= 64
    print(sums[n])
