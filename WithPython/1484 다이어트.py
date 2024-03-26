# 백준 1484 다이어트 골5

# G = 현재**2 - 기억하고 있던 몸무게**2

G = int(input())

# A**2 - B**2가 G가 될 수 있는지

# 최대 가능한것: 현재가 G, 이전 몸무게가 G-1까지만 가능

# (a+1) ** 2 - a**2 = 2a +1
# 최대 가능한거 -> (G-1) // 2
g = (G-1) // 2 + 1  # 최대 가능한거

l = 1
r = 1

answer = []
while l <= r and r <= g:
    result = r**2 - l**2
    if result > G:  # 너무 크다면
        l += 1
    elif result < G:
        r += 1
    elif result == G:
        answer.append(r)
        r += 1

# print(answer)
answer.sort()
if answer:
    for a in answer:
        print(a)
else:
    print(-1)
