# 백준 14658 하늘에서 별똥별이 빗발친다 골3

C, R, L, K = map(int, input().split())

# board = [[0 for _ in range(C)] for _ in range(R)]

stars = []

for _ in range(K):
    c, r = map(int, input().split())
    stars.append((r, c))
    # board[r-1][c-1] += 1

answer = 0

# 두 점을 선택해서 영역 만들기
for r1, c1 in stars:
    for r2, c2 in stars:
        minR = min(r1, r2)
        minC = min(c1, c2)

        cnt = 0
        # 다른 별이 그 영역 내에 있는지 count
        for r, c in stars:
            if minR <= r <= minR + L and minC <= c <= minC + L:
                cnt += 1

        answer = max(answer, cnt)

print(K - answer)
