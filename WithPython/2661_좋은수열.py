# 백준 2661 좋은수열 골4

N = int(input())


def check(arr):
    n = len(arr)
    for l in range(1, n//2 + 1):
        right = arr[n-l:]
        left = arr[n-2*l:n-l]
        # print("arr, left, right", arr, left, right)
        equal = True
        for i in range(l):
            if left[i] != right[i]:
                equal = False

        if equal:
            return False

    return True


def backTrack(depth):
    if depth == N:
        print(''.join(map(str, num)))
        exit()

    for i in range(1, 4):
        num.append(i)

        if check(num):
            backTrack(depth+1)

        # backTrack(depth + 1)
        num.pop()


num = []
backTrack(0)
