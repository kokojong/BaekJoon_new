# 백준 4883 삼각 그래프 실1

# 오른쪽, 아래, 대각아래(2가지) 만 가능
# 열 번호에 따라 조금 다르긴 함(조심)

T = 0
while True:
    T += 1
    N = int(input())

    if N == 0:
        break

    board = []
    for _ in range(N):
        row = list(map(int, input().split()))
        board.append(row)

    # print(board)

    dp = [[0 for _ in range(3)] for _ in range(N)]

    dp[1][0] = board[0][1]
    dp[1][1] = board[0][1]
    dp[1][2] = board[0][1]

    for i in range(2, N):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + board[i][0]
        dp[i][1] = min(min(dp[i-1]), dp[i-1][0] + board[i][0]) + board[i][1]
        dp[i][2] = min(dp[i-1][1], dp[i-1][2], dp[i][1]) + board[i][2]

    result = min(dp[-1]) + board[-1][1]
    print("%d. %d" % (T, result))
