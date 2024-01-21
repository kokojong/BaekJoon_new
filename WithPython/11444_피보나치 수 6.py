# 백준 11444 피보나치 수 6 골2

K = 100000007

# 피보나치 수에서 N번째

N = int(input())
K = 1000000007

# N번쨰의 피보나치 수의 행렬은 ( (1, 1) (1, 0) )의 N제곱을 한것의 [0][1]과 같다

fibos = [[1, 1], [1, 0]]


def multi(A, B):  # A와 B행렬의 곱셈
    n = len(A)
    tmp = [[0 for _ in range(n)] for _ in range(n)]

    for r in range(n):
        for c in range(n):
            cnt = 0

            for i in range(n):
                cnt += A[r][i] * B[i][c]
            tmp[r][c] = cnt % K

    return tmp


def square(A, k):
    n = len(A)
    if k == 1:
        for r in range(n):
            for c in range(n):
                A[r][c] %= K
        return A

    tmp = square(A, k//2)  # 거듭제곱을 logk로 줄여줌

    if k % 2:
        return multi(multi(tmp, tmp), A)  # A**2, A로 나눔
    else:
        return multi(tmp, tmp)


print(square(fibos, N)[0][1])
