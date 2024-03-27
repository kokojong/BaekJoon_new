# 백준 3649 로봇 프로젝트 골5

# 너비는 x, 두조각의 합은 정확하게 일치해야함.

while True:
    try:
        X = int(input()) * 10000000
        N = int(input())
        arr = []
        for _ in range(N):
            arr.append(int(input()))

        arr.sort()
        # print(arr)

        answer = []
        l = 0
        r = N-1

        while l < r:
            result = arr[l] + arr[r]

            if result < X:
                l += 1
            elif result == X:
                answer.append((arr[l], arr[r]))
                break
            elif result > X:
                r -= 1
        # print(answer)
        answer.sort(key=lambda x: abs(x[0] - x[1]))
        if answer:
            print('yes', answer[-1][0], answer[-1][1])
        else:
            print('danger')

    except:
        break
