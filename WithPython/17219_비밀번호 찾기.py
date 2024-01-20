# 백준 17219 비밀번호 찾기 실4

N, M = map(int, input().split())  # N - 사이트의 주소 수, M - 비밀번호를 찾으려는 주소 수

dic = dict()

for _ in range(N):
    site, pw = map(str, input().split())
    # print(site, pw)

    dic[site] = pw

for _ in range(M):
    print(dic[input()])
