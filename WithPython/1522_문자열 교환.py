# 백준 1522 문자열 교환 실1

arr = list(input().rstrip())
l = len(arr)
t = arr.count('a')

arr += arr  # 원형으로 만들기

answer = l
for i in range(0, l):
    cnt = arr[i:i+t].count('a')
    answer = min(answer, t-cnt)

print(answer)
