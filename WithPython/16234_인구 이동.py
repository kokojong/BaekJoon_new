# 백준 16234 인구 이동 골4

from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline


# N*N 땅
N, L, R = map(int, input().split())

board = []

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

answer = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def checkAll():  # 인구 이동이 필요하다면 True
    for r in range(N):
        for c in range(N):

            for i in range(4):
                rr = r + dr[i]
                cc = c + dc[i]

                # 차이가 L이상 R이하
                if 0 <= rr < N and 0 <= cc < N and L <= abs(board[rr][cc] - board[r][c]) <= R:
                    return True

    return False


def move():
    visited = [[-1 for _ in range(N)] for _ in range(N)]  # 속한 연합의 번호
    k = -1  # 연합 번호

    dic = defaultdict(list)

    for r in range(N):
        for c in range(N):
            queue = deque()
            if visited[r][c] == -1:
                k += 1
                queue.append((r, c))
                visited[r][c] = k
                dic[k].append(board[r][c])

            while queue:
                # print("queue", queue)
                qr, qc = queue.popleft()
                for i in range(4):
                    rr = qr + dr[i]
                    cc = qc + dc[i]

                    # 방문하지 않았음 + 아직 연합이 없음
                    if 0 <= rr < N and 0 <= cc < N and visited[rr][cc] == -1 and L <= abs(board[rr][cc] - board[qr][qc]) <= R:
                        # print("rr cc", rr, cc)
                        queue.append((rr, cc))
                        visited[rr][cc] = k
                        dic[k].append(board[rr][cc])

    # print("visited", visited)
    # print(dic)

    for r in range(N):
        for c in range(N):
            kk = visited[r][c]  # 연합의 번호
            board[r][c] = sum(dic[kk]) // len(dic[kk])

    # print(board)


while True:
    if checkAll():
        answer += 1
        move()
    else:
        break

print(answer)
