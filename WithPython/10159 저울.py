# 백준 10159 저울 골4
# 각 물건에 대해서 그 물건과의 비교 결과를 알 수 없는 물건의 개수를 출력하는 프로그램을 작성하시오.

N = int(input())
M = int(input())

# 나보다 큰거를 저장하는 배열
# 나보다 작은거를 저장하는 배열
big = [set() for _ in range(N+1)]
small = [set() for _ in range(N+1)]

board = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    # big[b].add(a)
    # small[a].add(b)
    board[a][b] = 1  # 내가 더 크다

# print(big)
# print(small)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][k] and board[k][j]:
                board[i][j] = 1
# print(board)

for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if not board[i][j] and not board[j][i]:
            cnt += 1
    print(cnt-1)
