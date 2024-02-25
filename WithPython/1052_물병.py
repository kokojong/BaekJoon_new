# 백준 1052 물병 실1

# N개의 물병에 각 1리터씩. 한번에 K개씩 옮김.
# 재분배 - 같은양의 물이 있는 2개 골라서 한쪽에 몰아주기

n, k = map(int, input().split())

answer = 0

while bin(n).count('1') > k:
    idx = bin(n)[::-1].index('1')  # 오른쪽에서 몇번쨰

    answer += (2**idx)
    n += (2**idx)

print(answer)
