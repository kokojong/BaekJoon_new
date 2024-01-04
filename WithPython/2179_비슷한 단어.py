# 백준 2179 비슷한 단어 골4

N = int(input())

words = []
for i in range(N):
    word = input()
    words.append([word, i])  # [word, 순서]

words.sort()

# print(words)


def check(a, b):
    cnt = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            cnt += 1
        else:
            return cnt
    return cnt


maxLength = 0
answers = []

lengthList = [[] for _ in range(N)]  # 각 원소별 가질수 있는 최대 길이, 그 문자열 저장

for i in range(N-1):
    cnt = check(words[i][0], words[i+1][0])
    print("cnt", cnt, words[i][0], words[i+1][0])
    if cnt >= maxLength:
        maxLength = cnt
        # [index1, word1] [index2, word2]
        tmp = [[words[i][1], words[i][0]], [words[i+1][1], words[i+1][0]]]
        tmp.sort(key=lambda x: x[0])

        # 각
        lengthList[i] = [cnt, words[i][0][:cnt]]
        print("1번", lengthList)
        lengthList[i+1] = [cnt, words[i+1][0][:cnt]]

        answers.append([cnt] + tmp)

print("lengthList", lengthList)

# for answer in answers:
#     print("answer", answer)
#     test = answer[1]
#     # print("test", test)
#     l, word1, word2 = answer[0], answer[1][1], answer[2][1]

#     # print(l, word1, word2)
#     if l == maxLength:
#         print(word1)
#         print(word2)
#         exit()

words.sort(key=lambda x: x[1])  # index 기준으로 다시 정렬
print("new words", words, lengthList)

first = ''

for i in range(N):
    if lengthList[i][0] == maxLength:
        if first == '':
            first = lengthList[i][1]
            print(words[i][0])
        elif lengthList[i][1] == first:
            print(words[i][0])
            break

# 9
# ab
# is
# lunch
# for
# most
# waits
# until
# two
# ac

# 4
# aa
# bb
# bc
# aj

# 답
# aa
# aj


# 5
# abab
# abaa
# abcdab
# abcda
# abcdaa

# 답
# abcdab
# abcda
