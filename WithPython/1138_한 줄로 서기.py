# 백준 1138 한 줄로 서기 실2

N = int(input())

arr = list(map(int, input().split()))

answer = [-1 for _ in range(N)]

for i in range(N):
    cnt = 0
    a = arr[i]

    for j in range(N):
        if cnt == a and answer[j] == -1:
            answer[j] = i + 1
            break

        elif answer[j] == -1:  # 빈자리
            cnt += 1

print(' '.join(map(str, answer)))
