# 백준 2302 극장 좌석 실1

# k명이 연속으로 된거에서 서로 자리를 바꿀수 있는 경우의수를 구해서 각각 곱하기??

N = int(input())
M = int(input())

dp = [1, 1, 2]  # 0에서 부터 시작

for i in range(3, 41):
    dp.append(dp[i-1] + dp[i-2])

start = 0
answer = 1
for _ in range(M):
    v = int(input())
    dif = v - start - 1
    start = v

    answer *= dp[dif]
    # print("dif, answer", dif, answer)

answer *= dp[N-start]

print(answer)
