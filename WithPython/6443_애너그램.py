# 백준 6443 애너그램 골5

from collections import defaultdict

N = int(input())


def backTrack(depth):
    if depth == len(arr):
        print(''.join(word))
        return

    for a in alphaDict.keys():
        if alphaDict[a]:  # 아직
            alphaDict[a] -= 1
            word.append(a)
            backTrack(depth + 1)
            word.pop()
            alphaDict[a] += 1


for _ in range(N):
    arr = list(input())
    arr.sort()  # 오름차순으로 나와야해서

    alphaDict = defaultdict(int)

    for a in arr:
        alphaDict[a] += 1  # 존재여부 - 있다!
    # print("alpha dict", alphaDict)
    word = []
    backTrack(0)
