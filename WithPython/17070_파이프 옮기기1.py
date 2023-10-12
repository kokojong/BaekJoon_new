# 백준 17070 파이프 옮기기 1 골5

import sys
input = sys.stdin.readline

N = int(input())

board = [[0 for _ in range(N+1)]]
for _ in range(N):
    row = [0] + list(map(int, input().split()))
    board.append(row)

# r, c에 가로/세로/대각선의 파이프가 연결된 끝 지점
dp1 = [[0 for _ in range(N+1)] for _ in range(N+1)]  # 가로
dp2 = [[0 for _ in range(N+1)] for _ in range(N+1)]  # 세로
dp3 = [[0 for _ in range(N+1)] for _ in range(N+1)]  # 대각선

dp1[1][2] = 1  # 처음 위치

for r in range(1, N+1):
    for c in range(2, N+1):
        if r == 1 and c == 2:
            continue

        if board[r][c] == 0:
            # 가로 (r, c-1)이 가로거나 대각선이어야만 가능
            dp1[r][c] = dp1[r][c-1] + dp3[r][c-1]
            # 세로 (r-1, c)이 세로거나 대각선이어야만 가능
            dp2[r][c] = dp2[r-1][c] + dp3[r-1][c]
            # 대각선 r-1,c 와 r,c-1이 비어있는지 먼저 확인하고 된다면 가로, 세로, 대각선 모두 가능
            if board[r-1][c] == 0 and board[r][c-1] == 0:
                dp3[r][c] = dp1[r-1][c-1] + dp2[r-1][c-1] + dp3[r-1][c-1]

answer = dp1[-1][-1] + dp2[-1][-1] + dp3[-1][-1]
print(answer)
