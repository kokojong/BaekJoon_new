# 백준 1629 곱셈 실1

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

# b를 반으로 나눠가면서 체크 -> 어차피 a^1에 수렴하게 된다

# 입력이 10 5 12
# (10^2 % 12) * (10^3 % 12) % 12

# 10^3 % 12 = (10^2 % 12) * (10^1 % 12)


def divide(a, b):
    if b == 1:
        return a % c

    div = divide(a, b//2)
    if b % 2 == 0:  # 짝수
        return (div * div) % c
    else:
        return (div * div * a) % c


print(divide(a, b))

# 처음에 생각한 내 풀이 -> 어차피 (a%c)한 결과와 또 a%c 를 곱하고 %c 를 할거니까 그대로 진행
# result = a
# while b > 0:
#     b -= 1

#     result %= c
#     result = result * result % c

# print(result)

# 시간초과 발생
