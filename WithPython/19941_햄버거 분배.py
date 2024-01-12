# 백준 19941 햄버거 분배 실3

N, K = map(int, input().split())
arr = list(input().rstrip())

# print(arr)

answer = 0
for i in range(N):
    if arr[i] == 'H':
        for k in range(-K, K+1):
            if 0 <= i+k < N and arr[i+k] == 'P':
                answer += 1
                arr[i] = ''
                arr[i+k] = ''
                # print("i+k", i, i+k)
                break

# print(arr)
print(answer)
