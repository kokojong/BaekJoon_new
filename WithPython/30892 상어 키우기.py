# 백준 30892 상어 키우기 실1

N, K, T = map(int, input().split())  # 최대 K마리, 현재 T

arr = list(map(int, input().split()))

arr.sort()

stack = []

for i in range(N):
    # print(i, stack, T)
    if arr[i] < T:  # 먹을 수 있음
        stack.append(arr[i])  # 일단 쌓아두고 생각하기

    else:
        # print("못먹음")
        # print(i, stack, T, arr[i])
        while stack and K > 0 and T <= arr[i]:
            T += stack.pop()
            K -= 1
        if arr[i] < T:
            stack.append(arr[i])

for _ in range(K):  # 남은거 만큼 pop
    if stack:
        T += stack.pop()
print(T)
