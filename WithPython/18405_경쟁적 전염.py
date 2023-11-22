# 백준 18405 경쟁적 전염

from collections import deque

N, K = map(int, input().split())  # 바이러스 종류

board = [[0 for _ in range(N)] for _ in range(N)]

# virus = deque()  # (번호, r, c)

tmp = []
for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] > 0:
            tmp.append((row[c], r, c))
            board[r][c] = row[c]
tmp.sort()
virus = deque(tmp)
# print(board)
# print(virus)

S, X, Y = map(int, input().split())  # s초 이후 x, y

# 매초마다 상하좌우로 증식(번호가 낮은것 부터 증식) 이미 바이러스가 있다면 다른 바이러스가 들어갈 수 없음

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for _ in range(S):
    tmp = []
    while virus:
        k, r, c = virus.popleft()
    # for k, r, c, in virus:  # 이미 번호순으로 정렬된 상태
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0 <= rr < N and 0 <= cc < N and board[rr][cc] == 0:
                # print("rr, cc", rr, cc, k)
                board[rr][cc] = k
                tmp.append((k, rr, cc))
    tmp.sort()
    virus = deque(tmp)

# print(board)
print(board[X-1][Y-1])
