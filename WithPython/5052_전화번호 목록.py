# 백준 5052 전화번호 목록 골4
import sys

t = int(input())

for _ in range(t):
    n = int(input())
    numbers = []
    for _ in range(n):
        # number = str(input())
        number = sys.stdin.readline().rstrip()
        numbers.append(number)

    numbers.sort()
    # print(numbers)
    answer = 'YES'
    for i in range(0, len(numbers) - 1):
        # 다음 자리에 있는애를 내 길이만큼 자름
        # print("aaa", numbers[i], numbers[i+1])
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            answer = 'NO'
            break

    print(answer)
