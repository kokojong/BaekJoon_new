# 백준 14501 퇴사 실3

N = int(input())

board = []
board.append([0, 0])

for _ in range(N):
    board.append(list(map(int, input().split())))

dp = [0 for _ in range(N+1+5)]  # 상담 일수는 5일이 최대

for i in range(N, 0, -1):  # N ~ 1 까지
    if board[i][0] + i - 1 <= N:  # 남은 일자에 가능한 일이라면
        # 지금거 선택 안한거 vs 선택하고 그 일수만큼 뒤로 간 dp + 보상
        dp[i] = max(dp[i+1], dp[i + board[i][0]] + board[i][1])
    else:
        dp[i] = dp[i+1]  # 불가능한거니까 이전값 그대로

print(dp[1])
