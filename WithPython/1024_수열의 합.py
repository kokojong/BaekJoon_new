# 백준 1024 수열의 합 실2

N, L = map(int, input().split())

# 합이 N이면서 길이가 L이상인 음이아닌 정수 리스트

# x+1 x+2 x+3 ... x+L 의 합이 N
# x*L + (L+1)*L / 2 = N

for i in range(L, 101):
    x = N - (i**2 + i) / 2

    if x % i == 0:  # 나눠떨어질때만
        m = int(x/i)

        if m >= -1:
            for j in range(1, i+1):
                print(m+j, end=' ')
            print()
            break
else:
    print(-1)
