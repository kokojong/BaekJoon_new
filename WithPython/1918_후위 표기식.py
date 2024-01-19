# 백준 1918 후위 표기식 골2

# 연산자의 우선순위에 따라 괄호를 묶어줌 -> 그다음에 괄호안의 연산자를 괄호의 오른쪽으로 옮김

arr = list(input().rstrip())

stack = []
answer = ''

for a in arr:

    if a not in ['(', ')', '+', '-', '*', '/']:
        answer += a
        continue

    if a == '(':
        stack.append(a)

    elif a in ['+', '-']:
        while stack and stack[-1] != '(':  # stack에서 괄호를 연게 아니라면 넣어주기
            answer += stack.pop()
        stack.append(a)

    elif a in ['*', '/']:
        # 또 곱셈이나 나눗셈이 있다면 걔는 stack에서 빼고 답에 더해준다
        while stack and stack[-1] in ['*', '/']:
            answer += stack.pop()
        stack.append(a)  # 다 끝났으면 stack에 더해준다

    else:  # ) 일때
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()  # ( 도 제거해버림

while stack:
    answer += stack.pop()

print(answer)
