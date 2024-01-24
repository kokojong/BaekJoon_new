# 백준 2665 미로 만들기 골4

# n*n 방 흰방만 들어갈 수 있음
# 0,0이 시작, n-1, n-1이 끝방
# 검은방 -> 흰방으로 바꿔야하는 최소의 수를 구하는것. 하나도 안바꾸면 0

from collections import deque
import heapq

N = int(input())

board = []
for _ in range(N):
    row = list(map(int, list(input().rstrip())))
    board.append(row)

# print(board)

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

# heap 풀이법(다익스트라)

# visited = [[0 for _ in range(N)] for _ in range(N)]

# heap = [(0, 0, 0)]  # cost, row, column

# while heap:
#     cost, r, c = heapq.heappop(heap)

#     # print("cost, r, c", cost, r, c)

#     if r == N-1 and c == N-1:
#         print(cost)
#         exit()

#     for i in range(4):
#         rr = r + dr[i]
#         cc = c + dc[i]

#         if 0 <= rr < N and 0 <= cc < N and visited[rr][cc] == 0:
#             visited[rr][cc] = 1

#             if board[rr][cc] == 0:
#                 heapq.heappush(heap, (cost + 1, rr, cc))  # 검은방이면 +1
#             else:
#                 heapq.heappush(heap, (cost, rr, cc))


# bfs 풀이법
visited = [[-1 for _ in range(N)] for _ in range(N)]

queue = deque()
queue.append((0, 0))  # cost는 visited에서 처리
visited[0][0] = 0

while queue:
    r, c = queue.popleft()

    if r == N-1 and c == N-1:
        print(visited[-1][-1])
        exit()

    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        if 0 <= rr < N and 0 <= cc < N and visited[rr][cc] == -1:

            if board[rr][cc] == 0:  # 검은거라면
                visited[rr][cc] = visited[r][c] + 1
                queue.append((rr, cc))  # 맨 뒤에 넣음
            else:
                visited[rr][cc] = visited[r][c]
                queue.appendleft((rr, cc))  # 우선적으로 앞에 넣음
