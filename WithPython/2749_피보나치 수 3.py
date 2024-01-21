# 백준 2749 피보나치 수 3

K = 10**6
N = int(input())

# idea: 패턴 찾기 -> 피사노 주기
# K = 10^k 라고 할 때 주기는 항상 15*10^(k-1)
k = 6  # 10의 6제곱이라서

fibos = [0, 1]
p = 15*(10**(k-1))
# print("p", p)

for i in range(2, p):
    fibos.append((fibos[i-1] + fibos[i-2]) % K)

print(fibos[N % p])  # 주기로 나눔
