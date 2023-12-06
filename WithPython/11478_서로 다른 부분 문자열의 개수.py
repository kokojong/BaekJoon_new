# 백준 11478 서로 다른 부분 문자열의 개수 실3

s = list(input())
n = len(s)

sets = set()

for i in range(0, n):
    for l in range(1, n-i+1):  # 길이
        arr = s[i:i+l]
        sets.add(''.join(arr))

print(len(sets))
