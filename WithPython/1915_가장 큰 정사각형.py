# 백준 1915 가장 큰 정사각형 골4

# 아이디어: 크기가 1인거부터 시작해서 dp를 구해줌(그 지점에서 시작하는걸로)
# 1씩 늘어날 때 마다 dp[i][j], (i,j+1), (i+1,j) (i+i, j+1) 이게 다 맞으면 디피 갱신?

R, C = map(int, input().split())

board = []
dp = [[0 for _ in range(C)] for _ in range(R)]

for _ in range(R):
    row = list(map(int, input().rstrip()))
    board.append(row)

l = 0  # 1로 두면 실패(다 0인경우)
for r in range(R):
    for c in range(C):
        if r == 0 or c == 0:
            dp[r][c] = board[r][c]
            continue

        if board[r][c] == 0:
            dp[r][c] = 0
            continue

        dp[r][c] = min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1]) + 1
    l = max(max(dp[r]), l)

# print(dp)
print(l * l)


# 시간초과 코드(디피같지만 디피같지 않은 ㅋㅋㅋ)
# l = 1  # 크기가 2인거 부터 체크

# while True:
#     l += 1

#     flag = False
#     for r in range(0, R):
#         for c in range(0, C):
#             if r+l-1 >= R or c+l-1 >= C:
#                 dp[r][c] = 0

#             if dp[r][c] == 0:
#                 continue

#             if dp[r][c+1] and dp[r+1][c] and dp[r+1][c+1]:
#                 dp[r][c] = 1
#                 flag = True
#             else:
#                 dp[r][c] = 0
#                 dp[r]
#     if not flag:
#         break
# # print(dp)
# print(l-1)
