# 백준 12015 가장 긴 증가하는 부분 수열 2 골2

# 기존의 dp로 푸는 문제가 아니고 10*6의 크기기 때문에 시간 초과가 나게 된다

# 검색해 보고 얻은 풀이법! -> 하나씩 원소에 접근해가면서 (O(N)) LIS[-1]보다 크다면 LIS에 넣고 진행
# 더 작다면 이전의 LIS에서 들어갈 수 있는(다음 인덱스가 나보다 커지는) 위치를 찾아서 바꿔치기
# idea로는 중간에 실제로 만들어 질 수 없는 LIS이어도 수열의 길이가 더 중요하기 때문에 그냥 이어나감(이해하기 어려움)

import sys
input = sys.stdin.readline

N = int(input())

LIS = [0]  # 일단 0이 들어감

arr = list(map(int, input().split()))


def findIndex(target, l):
    left = 1
    right = l

    while left <= right:
        # 실수한 부분.. 얘를 while문 밖에 빼둬서 mid에 계속 같은거만 들어갔음 ^^
        mid = (left+right) // 2
        if LIS[mid] == target:
            # right = mid - 1
            return mid
        elif LIS[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left


for i in range(N):
    if arr[i] > LIS[-1]:
        LIS.append(arr[i])
    else:
        idx = findIndex(arr[i], len(LIS))
        LIS[idx] = arr[i]

# print(LIS)
print(len(LIS) - 1)
