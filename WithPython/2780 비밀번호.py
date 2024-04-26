# 백준 2780 비밀번호 실1

T = int(input())

# N <= 1000 -> 미리 만들어두기
dp = [[0 for _ in range(10)] for _ in range(1001)]
dp[1] = [1 for _ in range(10)]
arr = [[7], [2, 4], [1, 3, 5], [2, 6], [1, 5, 7], [
    2, 4, 6, 8], [3, 5, 9], [0, 4, 8], [5, 7, 9], [6, 8]]

for i in range(2, 1001):
    for j in range(10):
        for a in arr[j]:
            dp[i][j] += dp[i-1][a]

# print(dp)
# print(sum(dp[1]))
# print(sum(dp[2]))
# print(sum(dp[3]))

for _ in range(T):
    K = int(input())
    print(sum(dp[K]) % 1234567)

# 1000 -> 689038이 나와야함
