import sys
S = set()

M = int(sys.stdin.readline())

for _ in range(M):
    command = sys.stdin.readline().strip().split()

    if len(command) == 1:
        if command[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()

    else:
        func, x = command[0], command[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
