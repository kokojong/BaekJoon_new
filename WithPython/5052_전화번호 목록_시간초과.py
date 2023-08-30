# 백준 5052 전화번호 목록 골4

t = int(input())

for _ in range(t):
    answer = 'YES'
    n = int(input())

    numbers = []
    minLength = 10
    maxLength = 0

    dic = {}

    for _ in range(n):
        number = str(input())
        numbers.append(number)
        dic[number] = number
        minLength = min(minLength, len(number))
        maxLength = max(maxLength, len(number))

    # print(numbers)
    # print(minLength)

    for number in numbers:
        # 길이가 minLengh 이상인거로 잘라보기
        l = len(number)
        for length in range(minLength, l+1):  # 최소 길이 ~ number의 길이까지
            part = number[0:length]  # 해당 길이만큼 다 잘랐었는데 문제를 자세히 보니 '접두어'였음
            # 본인의 dic이면 안되니까 같은 길이가 아닐때로 제한
            # print("aaa", part, l)
            if part in dic and l != len(part):
                # print("nonono")
                answer = 'NO'
                break

    print(answer)
