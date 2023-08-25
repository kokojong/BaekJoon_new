# 백준 1987 알파벳 골4

# 아마도 백트래킹..? (dfs)

# 지금까지 나온걸 딕셔너리에 계속 더해주면 될듯(배열로 처리하면 시간 복잡도가 증가)

# 억까0 python으로 하면 시간초과가 나서 Pypy3
# 억까1 setrecursionlimit으로 하면 메모리 오류남(조건이 엄청 빡빡해서 그거보다 많이 되면 안되는 듯)
# 억까2 sys.stdin.readline으로 받고 rstrip을 했더니 시간초과가 나옴 ㅎㅎㅎ..ㅎ.ㅎ.ㅎ.ㅎ.ㅎ..
# 억까3 디폴트 딕셔너리 써봤는데 시간초과남 ㅎ.. -> 그냥 set을 써야함

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6) -> 얘를 써주면 메모리 초과가 난다 왜일까...?

from collections import defaultdict

R, C = map(int, input().split())

board = []
answer = 0

for _ in range(R):
    row = list(map(str, input()))
    board.append(row)

visited = set()
# visited = defaultdict(bool)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(r, c, depth):  # visited를 같이 파라미터로 넘겼더니 시간초과 발생. pypy3에서는 메모리 초과 발생
    global answer
    answer = max(answer, depth)

    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        if 0 <= rr < R and 0 <= cc < C and not board[rr][cc] in visited:
            # if 0 <= rr < R and 0 <= cc < C and visited[board[rr][cc]] == False:
            # newVisited = copy.deepcopy(visited)
            # newVisited[board[rr][cc]] = True
            # print("rr, cc, newVisited", rr, cc, newVisited)
            # dfs(rr, cc, newVisited, depth + 1)

            visited.add(board[rr][cc])
            # visited[board[rr][cc]] = True
            dfs(rr, cc, depth + 1)
            visited.remove(board[rr][cc])
            # visited[board[rr][cc]] = False


visited.add(board[0][0])
# visited[board[0][0]] = True
dfs(0, 0, 1)

print(answer)
