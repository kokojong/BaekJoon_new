# 백준 1083 소트 골5

N = int(input())
arr = list(map(int, input().split()))
S = int(input())

# 내 위치에서 뒤에를 체크해줌
for i in range(N):
    end = min(N-1, i+S)  # 바꿀수 있는 가장 끝점의 index
    maxV = max(arr[i:end+1])  # i~end 까지 중에서 가장 큰애를 찾아봄
    idx = arr.index(maxV)

    # swap
    for j in range(idx, i, -1):  # 앞에 애랑 바꿔주기
        arr[j], arr[j-1] = arr[j-1], arr[j]
        S -= 1

    if S == 0:
        break
print(*arr)
