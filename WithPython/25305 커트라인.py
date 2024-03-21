# 백준 25305 커트라인 브2

N, K = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort(reverse=True)

print(arr[K-1])
