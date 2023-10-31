# 백준 14890 경사로 골3

# 모든 칸의 높이가 모두 같거나 경사로
# 경사로의 높이는 1, 길이는 L

# 강사로는 낮은칸에 놓으며 L개의 연속된 칸에 경사로 바닥이 접해야함
# 낮은칸과 높은칸의 높이차이는 1
# 경사로를 놓을 칸의 높이는 모두 같아야하고 L개의 칸이 연속되어야함
# 경사로는 무한대로 가능

import sys
input = sys.stdin.readline

N, L = map(int, input().split())

board = []

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)


todo = []

for i in range(N):
    row = board[i]
    todo.append(row)

for c in range(N):
    column = []
    for r in range(N):
        column.append(board[r][c])
    todo.append(column)


answer = 0

# def check(arr):
#     visited = [False for _ in range(N)]

#     for i in range(N - 1):
#         if arr[i] == arr[i+1]:
#             continue

#         if abs(arr[i] - arr[i+1]) > 1:  # 차이가 너무 큼
#             return False

#         if arr[i] > arr[i+1]:
#             next = arr[i+1]

#             for j in range(i+1, i+1+L):
#                 if j >= N or j < 0:
#                     return False
#                 if arr[j] != next:
#                     return False
#                 if visited[j]:
#                     return False
#                 visited[j] = True

#         else:
#             next = arr[i]

#             for j in range(i, i-L, -1):
#                 if j >= N or j < 0:
#                     return False
#                 if arr[j] != next:
#                     return False
#                 if visited[j]:
#                     return False
#                 visited[j] = True
#     return True


# for t in todo:
#     if check(t):
#         answer += 1
# print(answer)

def checkIfNeed(arr, now):  # 이미 다 같은건지만 체크
    for k in range(1, L+1):
        next = now + k

        if arr[now] != arr[next]:
            return True

    return False  # L만큼의 길이의 배열이 다 평평함


def checkUp(arr, now):
    # 다음으로 L-1개만큼은 나랑 똑같고 L번째는 1 커야함
    for k in range(1, L):
        next = now + k

        if arr[next] != arr[now]:
            return False

    if arr[now+L] == arr[now] + 1:
        return True

    return False


def checkDown(arr, now):
    #
    for k in range(1, L+1):
        next = now + k
        # print("down", arr[now], arr[next])
        if arr[next] != (arr[now] - 1):
            return False

    return True


def checkPart(arr, now):  # 검사가 가능한것인지 체크
    for k in range(1, L+1):  # 길이가 L인 경사로
        next = now + k

        if next >= N:  # 크기가 넘어가버림
            return False

        if abs(arr[next] - arr[now]) >= 2:  # 경사로를 둘 수 없음(크기가 1보다 크게 차이남)
            return False

    return True


for t in todo:
    # 길이가 N인 array임
    result = True

    visited = [False for _ in range(N)]
    for i in range(N-L):
        # i <= N-L-1: # i는 시작점
        # print(c, checkIfNeed(t, i), checkPart(t, i))

        if visited[i]:
            continue

        if not checkPart(t, i):  # 차이가 너무 크거나 범위를 벗어나면
            result = False
            break

        if not checkIfNeed(t, i):
            continue

        print(t, t[i:i+L+1], i, "check", checkUp(t, i), checkDown(
            t, i))

        if checkUp(t, i):  # 오르막or내리막 가능하다면
            for k in range(i, i+L):  # 오르막 -> i부터 L개
                visited[k] = True  # 경사로를 넣어버림
            continue
        elif checkDown(t, i):
            for k in range(i+1, i+L+1):  # 내리막 -> i+1부터 L개
                visited[k] = True
            continue
        else:
            result = False
            break

    if result:
        print("가능", t)
    else:
        print("불가능", t)
    answer += result

print(answer)

# 가능 [2, 2, 2, 3, 2, 3] -> 이게 문제
