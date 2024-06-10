# 백준 7795 먹을것인가 먹힐것인가 실3

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    start = 0
    answer = 0

    for i in range(N):
        while True:
            if start == M or A[i] <= B[start]:
                answer += start
                break
            else:
                start += 1

    print(answer)
