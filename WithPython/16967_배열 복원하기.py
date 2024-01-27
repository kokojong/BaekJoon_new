# 백준 16967 배열 복원하기 실3

H, W, X, Y = map(int, input().split())

# H+X * W+Y 으로 이동한거로 한다 이때 겹쳐진건 합쳐짐
# 아래로 X칸, 오른쪽으로 Y칸

# A를 모르는 상태로 B를 가지고 구하기

B = []

for _ in range(H + X):
    row = list(map(int, input().split()))
    B.append(row)

A = [[0 for _ in range(W)] for _ in range(H)]

for r in range(H):
    for c in range(W):
        A[r][c] = B[r][c]

for r in range(X, H):
    for c in range(Y, W):
        A[r][c] = B[r][c] - A[r-X][c-Y]

for r in range(H):
    print(*A[r])
