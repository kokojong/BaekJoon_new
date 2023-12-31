# 백준 1863 스카이라인 쉬운거 골4

n = int(input())

arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append(y)

arr.append(0)  # 끝나는 지점 처리

stack = [0]
answer = 0

for a in arr:
    height = a
    # 더 큰 빌딩이 오면 패쓰
    if stack[-1] < a:
        stack.append(a)
        continue

    while stack[-1] > a:
        if stack[-1] != height:
            answer += 1
            height = stack[-1]

        stack.pop()
    stack.append(a)

print(answer)
