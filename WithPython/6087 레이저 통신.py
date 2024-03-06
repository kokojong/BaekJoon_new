# 백준 6087 레이저 통신 골3

# W * H크기의 지도
# C로 표시된 칸이 2칸. 얘네들끼리 통신하기 위해서 설치해야하는 거울 개수의 최솟값
# / 또는 \ 를 만나면 90도 틀어짐

# idea -> C에서 bfs를 돌리는데 방향 정보도 같이 저장해보기? -> 최단 거리일때 경로를 보고 방향이 몇번 바뀐건지 체크하기

from collections import deque

W, H = map(int, input().split())

board = []

for _ in range(H):
    row = list(input())
    board.append(row)

starts = []

for r in range(H):
    for c in range(W):
        if board[r][c] == 'C':
            starts.append((r, c))

start = starts[0]
end = starts[1]


def BFS(r, c):
    global visited

    queue = deque()
    queue.append((r, c))
    visited[r][c] = 0

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while queue:
        r, c = queue.popleft()

        if (r, c) == end:
            answer = min(visited[r][c], answer)

        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            while True:  # 한쪽 방향씩 끝까지 가봄

                if not (0 <= rr < H and 0 <= cc < W):
                    break

                if board[rr][cc] == '*':
                    break

                if visited[rr][cc] < visited[r][c] + 1:
                    break  # 원래 경로가 더 최소일 때

                queue.append((rr, cc))
                visited[rr][cc] = visited[r][c] + 1  # 여기에 거울을 설치한거라서 + 1

                # 다음 칸으로 이동(같은 방향)
                rr += dr[i]
                cc += dc[i]


visited = [[float('inf') for _ in range(W)] for _ in range(H)]
answer = float('inf')
BFS(start[0], start[1])
print(answer)
