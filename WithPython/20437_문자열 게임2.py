# 백준 20437 문자열 게임2 골5

from collections import defaultdict

T = int(input())

# 어떤 문자를 k개 포함하는 가장 짧은 연속 문자열의 길이
# 이중에서 첫번째와 마지막 글자가 같은 가장 긴 연속 문자열

for _ in range(T):
    w = list(input().rstrip())
    k = int(input())

    dic = defaultdict(list)
    # 알파벳: 해당 위치

    for i in range(len(w)):
        dic[w[i]] += [i]

    # 3번
    minLen = len(w)

    # 4번
    maxLen = 1

    isChecked = False  # 결과가 있는지

    for (alpha, indexes) in dic.items():
        indexList = sorted(indexes)
        if len(indexes) >= k:
            for i in range(len(indexes) - k + 1):
                tmp = indexList[i + k - 1] - indexList[i] + 1  # 길이?
                isChecked = True
                minLen = min(minLen, tmp)
                maxLen = max(maxLen, tmp)

    # 원래는 minLen == len(w)라고 했는데 최대 길이에서 조건을 만족할수도 있음을 인지하지 못함
    if not isChecked:  # 못찾은거면
        print(-1)
        continue

    print(' '.join(map(str, [minLen, maxLen])))
