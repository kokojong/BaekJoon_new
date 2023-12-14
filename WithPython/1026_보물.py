# 백준 1026 보물 실4

N = int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort(reverse=True)

answer = 0
for i in range(N):
    answer += arr1[i] * arr2[i]

print(answer)
