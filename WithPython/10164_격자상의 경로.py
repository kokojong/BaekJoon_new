# 백준 10164 격자상의 경로 실1

# O 표시된 칸이 1개거나 없거나

# 조건1 - 오른쪽 or 아래로만 이동가능
# 조건2 - 격자에 O로 된 칸이 있다면 반드시 지나가야한다
# 이 조건을 만족하면서 이동할 수 있는 경로가 몇개인지 찾기

R, C, K = map(int, input().split())

dp = [[1 for _ in range(C)] for _ in range(R)]

if not K == 0:
    rr = K // C
    cc = K % C - 1

    for r in range(1, R):
        for c in range(1, C):
            a = dp[r-1][c]
            b = dp[r][c-1]

            dp[r][c] = a+b

    k = dp[rr][cc]

    for r in range(rr, R):
        for c in range(cc, C):
            dp[r][c] = k

    for r in range(rr+1, R):
        for c in range(cc+1, C):
            a = dp[r-1][c]
            b = dp[r][c-1]

            dp[r][c] = a+b
    print(dp[-1][-1])

else:
    for r in range(1, R):
        for c in range(1, C):
            a = dp[r-1][c]
            b = dp[r][c-1]

            dp[r][c] = a+b
    print(dp[-1][-1])
