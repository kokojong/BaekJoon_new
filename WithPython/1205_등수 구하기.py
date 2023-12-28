# 백준 1205 등수 구하기 실4

N, point, P = map(int, input().split())

if N <= 0:
    print(1)
    exit()

arr = list(map(int, input().split()))

if N == P and arr[-1] >= point:
    print(-1)
else:
    result = N+1  # 가장 맨 뒤 등수로 일단 초기화
    for i in range(N):
        if arr[i] <= point:
            result = i+1
            break
    print(result)
