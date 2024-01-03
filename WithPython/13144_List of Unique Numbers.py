# 백준 13144 List of Unique Numbers 골4

# 1개 이상의 수를 뽑았을 때 같은수가 없도록!

# 단순히 모두 확인하게 되면 10만 * 10만으로 시간초과 발생
# 투포인터로 처리하기

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

l = 0
r = 0

answer = 1

numbers = set()
numbers.add(arr[0])

while l < N and r < N:  # 1개인것도 되기 때문에 left, right가 같아도 된다

    if r+1 < N:
        if arr[r+1] not in numbers:  # 바로 오른쪽으로 확장이 가능하다면
            numbers.add(arr[r+1])
            r += 1
            # print("add 성공", numbers)
            answer += (r - l + 1)  # set의 크기
        else:
            numbers.remove(arr[l])
            l += 1
            # print("add 실패", numbers)

    else:  # r이 이미 끝에 도달
        numbers.remove(arr[l])
        l += 1
        # print("left 성공", numbers)

print(answer)
