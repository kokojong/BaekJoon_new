# 백준 9465 스티커 실1

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # idea: dp[i][j] 에서 골랐을때와 안골랐을 때를 저장해두고 그걸 하나식 지나가면서 마지막에 최대값?
    # 안골랐을 때, 골랐을때로 디피를 3차원 배열 하려고 했는데 아니었따 ㅜ
    n = int(input())
    # dp = [[0 for _ in range(n)] for _ in range(2)]

    dp = []
    dp.append(list(map(int, input().split())))
    dp.append(list(map(int, input().split())))
    # dp[i][j][1] = 옆에 있는거 다 안골랐을때 + 골랐을 때 얻는거

    # 해설 참고 -> 지그재그로 가기 or 한줄 건너뛰고 안 지그재그인거 고르기

    if n > 1:  # 한 열로 끝나는게 아니라면
        dp[0][1] += dp[1][0]  # 지그재그
        dp[1][1] += dp[0][0]

    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))
