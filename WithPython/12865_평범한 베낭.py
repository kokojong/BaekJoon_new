# 백준 12865 평범한 베낭

# 예전에 풀었지만 모르겠고 유명한 유형이라 다시 ㄱㄱ

N, K = map(int, input().split())

dp = [[0 for _ in range(K+1)] for _ in range(1+N)]

for r in range(1, N+1):  # 물품을 하나씩 돌면서
    w, v = map(int, input().split())
    for c in range(1, K+1):
        if c >= w:  # 얘를 담을 수 있는 위치라면
            # 담을수 있으나 안담음(r-1 ,c) vc 댬음 -> 담은 만큼 이전으로 돌아간 dp + v
            dp[r][c] = max(dp[r-1][c], dp[r-1][c-w] + v)
        else:
            dp[r][c] = dp[r-1][c]

print(dp[N][K])
