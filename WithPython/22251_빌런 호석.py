# 백준 22251 빌런 호석 골5

# K 자리수

# 최대 P개를 반전시키기
# 반전 이후에는 올바른 수가 보여지게 해야함(1~N사이)

# 실제로 X층일때 반전시킬 LED를 고를 수 있는 경우의 수


# N 층까지 가능, k자리수, 최대 반전 P개, 실제 X

# digit으로 변환하기

digitals = [
    0b1111110,  # 0
    0b0110000,
    0b1101101,
    0b1111001,
    0b0110011,
    0b1011011,  # 5
    0b1011111,
    0b1110000,
    0b1111111,
    0b1111011  # 9
]

# 반전에 필요한 갯수


def countXor(a, b):
    result = 0
    # l = digitals[a] ^ digitals[b]
    # print("l", l)
    for r in list(bin(digitals[a] ^ digitals[b])):
        if r == "1":
            result += 1
    return result


# 9 1 2 5
N, K, P, X = map(int, input().split())

answer = 0

for i in range(1, N+1):
    target = str(i).zfill(K)  # 이 숫자랑 X랑 비교
    now = str(X).zfill(K)

    cnt = 0
    for k in range(K):
        cnt += countXor(int(target[k]), int(now[k]))  # 자리별로 비교

    if cnt >= 1 and cnt <= P:
        answer += 1

print(answer)
