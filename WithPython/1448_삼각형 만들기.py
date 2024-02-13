# 백준 1448 삼각형 만들기 실3

N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

# 최대의 삼각형이 되려면 가장큰 3개씩 골라서 봐야함(슬라이딩 윈도우)

answer = -1

for i in range(N-2):
    c = arr[i]
    b = arr[i+1]
    a = arr[i+2]
    if c < a + b:
        answer = max(c+b+a, answer)
        break

print(answer)
