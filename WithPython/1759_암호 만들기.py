# 백준 1759 암호 만들기 골5

L, C = map(int, input().split())  # 만들어야하는 길이 L, 알파벳수 C

aeiou = ['a', 'e', 'i', 'o', 'u']

# 최소 1개 모음, 최소 2개 자음

arr = list(input().split())
arr.sort()

visited = [False for _ in range(C)]


def backTrack(idx, depth):
    if depth == L:
        c = len(set(aeiou) & set(word))
        if c >= 1 and L - c >= 2:
            print(''.join(word))

    else:
        for i in range(idx, C):
            word.append(arr[i])
            backTrack(i+1, depth + 1)
            word.pop()


word = []
backTrack(0, 0)
