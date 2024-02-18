# 백준 13270 피보나치 치킨 2 실2

# 인원수 -> 이에 맞게 치킨을 배분(?)

# 2인 1닭, 3인 2닭 5인 3닭 이런식

fivo = [0, 1]

N = int(input())

for i in range(2, N+1):
    fivo.append(fivo[i-1] + fivo[i-2])

# print(fivo)

# fivo[i] 명 -> fivo[i-1]닭

dpMin = [10000 for _ in range(N+1)]
dpMin[0] = 0
dpMin[1] = 1
dpMin[2] = 1
dpMax = [0 for _ in range(N+1)]

# if N >= 3:
if N == 2:
    print(1, 1)
    exit()

if N == 3:
    print(2, 2)
    exit()

k = 3

while True:
    if k > N:
        break
    a = fivo[k-1]  # 닭 수
    b = fivo[k]  # 인원수

    for i in range(b, N+1):
        dpMin[i] = min(dpMin[i-b] + a, dpMin[i])
        dpMax[i] = max(dpMax[i-b] + a, dpMax[i])

    k += 1

print(dpMin[N], dpMax[N])
