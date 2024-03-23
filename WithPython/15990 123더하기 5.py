# 백준 15990 123 더하기 5 실2

# 같은 수를 두번이상 연속 사용 불가

T = int(input())
K = 1_000_000_009

M = 100000  # 최대
dp1 = [0 for _ in range(M+1)]
dp2 = [0 for _ in range(M+1)]
dp3 = [0 for _ in range(M+1)]

# 각각 숫자로 끝나는 디피의 갯수
dp1[1] = 1  # 1
dp1[3] = 1  # 2+1

dp2[2] = 1  # 2
dp2[3] = 1  # 1+2

dp3[3] = 1  # 3

# 4의 경우 -> dp3[3] + dp2[2] + dp1[1]

for i in range(4, M+1):
    dp1[i] = (dp2[i-1] + dp3[i-1]) % 1_000_000_009
    dp2[i] = (dp1[i-2] + dp3[i-2]) % 1_000_000_009
    dp3[i] = (dp1[i-3] + dp2[i-3]) % 1_000_000_009

for _ in range(T):
    N = int(input())
    print((dp1[N] + dp2[N] + dp3[N]) % 1_000_000_009)
