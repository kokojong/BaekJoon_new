# 백준 2138 전구와 스위치 골5

import copy

N = int(input())

arr = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))

newArr = copy.deepcopy(arr)
newArr[0] = (newArr[0] + 1) % 2
newArr[1] = (newArr[1] + 1) % 2


def change(arr, count):
    for i in range(1, N-1):
        if arr[i-1] != target[i-1]:
            count += 1
            for j in range(3):  # 3개 뒤집기
                arr[i-1 + j] = (arr[i-1 + j] + 1) % 2

    if arr[N-1] != target[N-1]:
        count += 1
        arr[N-1] = (arr[N-1] + 1) % 2
        arr[N-2] = (arr[N-2] + 1) % 2

    # print("arr, target", arr, target)
    if arr == target:
        return count
    else:
        return -1


result1 = change(arr, 0)
result2 = change(newArr, 1)

# print(result1, result2)

if result1 < 0 and result2 < 0:
    print(-1)
elif result1 >= 0 and result2 >= 0:
    print(min(result1, result2))
else:
    print(max(result1, result2))
