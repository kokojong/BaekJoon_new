# 백준 1263 시간관리 골5

N = int(input())

arr = []
last = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        print(-1)
        exit()
    arr.append([a, b])
    last = max(b, last)

# arr.sort(key=lambda x: (x[1], -x[0]))  # 끝나는게 이른거 부터, 그리고 필요한 시간이 오래걸리는거 부터
arr.sort(key=lambda x: (-x[1], -x[0]))
# print(arr)

visited = [0 for _ in range(last+1)]

for i in range(N):
    a, b = arr[i]

    posible = False
    for k in range(b, 0, -1):  # 끝점으로 체크하기
        tmp = visited[k-a+1:k+1]
        # print("k, tmp", k, tmp)
        if sum(tmp) == 0:
            posible = True
            for j in range(k-a+1, k+1):  # 가능하다면 걔네들 다 1로 만들기
                visited[j] = 1
            break
    if posible == False:
        print(-1)
        exit()
# print(visited)
# 4
# 5 10
# 4 10
# 1 10
# 2 3

# 3
# 5 10
# 3 10
# 1 10

# 1
# 10 8

answer = 0
for i in range(0, last+1):
    if visited[i] == 0:
        answer = i
    else:
        break

print(answer)
