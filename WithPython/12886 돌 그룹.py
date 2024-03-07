# 백준 12886 돌 그룹 골4

# 3개 그룹 -> 모든 돌 개수를 같게 만들기
# 작은거 X 큰거 Y, X+X, Y-X개로 만듬
# 얘네들을 같은 개수로 만들수 있는지 체크 1 or 0

from collections import deque

A, B, C = map(int, input().split())
total = A + B + C

if total % 3 != 0:
    print(0)
    exit()

# idea: 1보다 크게 차이나는애들을 골라서 평탄화(?)를 함. -> 그래도 안되는거면 안되는것


def BFS():
    # 최댓값, 최솟값 -> 나머지는 total에서 빼면댐
    visited = [[False for _ in range(total)] for _ in range(total)]

    queue = deque()
    queue.append((A, B))
    visited[A][B] = True

    while queue:
        a, b = queue.popleft()
        c = total - a - b

        if a == b == c:
            print(1)
            exit()

        for X, Y in [(a, b), (b, c), (a, c)]:
            if X == Y:
                continue
            if X > Y:
                X, Y = Y, X  # 교체

            Y -= X
            X += X

            minV = min(X, Y, total - X - Y)
            maxV = max(X, Y, total - X - Y)

            if visited[minV][maxV]:
                continue

            queue.append((minV, maxV))
            visited[minV][maxV] = True


BFS()
print(0)
