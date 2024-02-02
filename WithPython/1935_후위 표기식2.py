# 백준 1935 후위 표기식2 실3

from collections import defaultdict

N = int(input())

arr = list(input().rstrip())

dic = defaultdict(int)

start = ord('A')
for i in range(N):
    dic[chr(i + start)] = int(input())

stack = []

print(dic)

for a in arr:
    if not stack:
        stack.append(dic[a])
    else:
        if a in ['+', '-', '*', '/']:
            a2 = stack.pop()
            a1 = stack.pop()

            # print("a1, a2", a1, a2)

            if a == '+':
                result = float(a1) + float(a2)
            elif a == '-':
                result = float(a1) - float(a2)
            elif a == '*':
                result = float(a1) * float(a2)
            elif a == '/':
                result = float(a1) / float(a2)

            stack.append(result)
        else:
            stack.append(dic[a])


print('%.2f' % stack[0])
