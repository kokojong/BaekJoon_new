# 백준 2504 괄호의 값 골5

arr = list(map(str, input()))


def check():
    stack = []

    for i in range(len(arr)):
        if not stack:
            stack.append(arr[i])
            continue

        if arr[i] == ')':
            if stack[-1] == '(':
                stack.pop()
                continue

        if arr[i] == ']':
            if stack[-1] == '[':
                stack.pop()
                continue

        stack.append(arr[i])

    if stack:
        return False
    else:
        return True


def calcu():
    answer = 0
    tmp = 1

    stack = []

    for i in range(len(arr)):
        a = arr[i]
        if a == '(':
            stack.append(a)
            tmp *= 2
        elif a == '[':
            stack.append(a)
            tmp *= 3
        elif a == ')':
            if i > 0 and arr[i-1] == '(':  # 제일 안쪽일때(안에 더 없음)
                answer += tmp
            stack.pop()
            tmp //= 2  # 2로 나눠줌
        elif a == ']':
            if i > 0 and arr[i-1] == '[':  # 제일 안쪽일때(안에 더 없음)
                answer += tmp
            stack.pop()
            tmp //= 3

    return answer


if check() == False:
    print(0)
    exit()
else:
    print(calcu())
