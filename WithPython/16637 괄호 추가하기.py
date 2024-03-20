# 백준 16637 괄호 추가하기 골3

from itertools import combinations

N = int(input())  # 1~19 -> 연산자는 최대 9개! 9개중에 k개씩 선택해가며 가능여부 판단

arr = list(input())  # 0 ~ N-1 까지의 index, 그중에 홀수가 연산자

posibles = []

opers = [(2*i+1) for i in range(N//2)]  # 연산자들의 index

for k in range(len(opers) + 1):
    comb = list(combinations(opers, k))

    # print("comb", comb)

    for com in comb:
        isPosible = True
        last = -4
        for c in com:
            if c >= last + 4:
                last = c
            else:
                isPosible = False

        if isPosible:
            posibles.append(com)

answer = -float('inf')


def calcu(a, b, op):
    a = int(a)
    b = int(b)
    if op == "+":
        return str(a+b)
    elif op == "-":
        return str(a-b)
    elif op == "*":
        return str(a*b)


for posible in posibles:
    # 이 번호들의 opers에 괄호를 친다
    result = 0

    stack = []

    i = 0
    while i < N:
        if i % 2 == 0:  # 숫자들
            # if not stack:
            stack.append(arr[i])
            i += 1
            # else:

        else:
            if i in posible:
                a = stack.pop()
                op = arr[i]
                b = arr[i+1]
                c = calcu(a, b, op)
                stack.append(c)
                i += 2

            else:
                stack.append(arr[i])
                i += 1
    # print(posible)
    # print(stack)

    now = stack[0]

    for i in range(1, len(stack)):
        if i % 2 == 1:
            now = calcu(now, stack[i+1], stack[i])

    # print("now", now)
    answer = max(int(now), answer)
print(answer)
