# 백준 1722 순열의 순서 골5

N = int(input())

ins = list(map(int, input().split()))
A = ins[0]
arr = ins[1:]

sets = {}

# set에다가 몇째자리에 몇인지 저장해둠.


def find_permutations(n):
    if n in sets:
        return sets[n]

    elif n <= 1:
        return 1

    else:
        sets[n] = n * find_permutations(n - 1)
        return sets[n]


if A == 1:
    K = arr[0]  # K 번째거를 찾기
    tmp = [i for i in range(1, N+1)]

    answer = []

    for i in range(N):
        p = find_permutations(N-i-1)
        step = (K-1)//p
        answer.append(tmp[step])
        tmp.remove(tmp[step])
        K -= p * step

    print(*answer)

else:
    # arr # arr를 가지고 얘가 몇번째인지 찾기
    sortedArr = sorted(arr)
    answer = 1

    for i in range(N):
        step = sortedArr.index(arr[i])
        sortedArr.remove(arr[i])
        x = find_permutations(N - 1 - i)
        answer += x * step

    print(answer)

# print("sets", sets)
