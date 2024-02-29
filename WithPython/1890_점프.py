# 백준 1890 점프 실1

# N * N
# 각 칸에서 갈수있는 거리
# 오른쪽이나 아래로만 이동가능

N = int(input())

board = []

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

dr = [1, 0]
dc = [0, 1]

for r in range(N):
    for c in range(N):

        if r == N-1 and c == N-1:
            print(dp[-1][-1])
            break

        for i in range(2):
            rr = r + dr[i] * board[r][c]
            cc = c + dc[i] * board[r][c]

            if 0 <= rr < N and 0 <= cc < N:
                dp[rr][cc] += dp[r][c]
