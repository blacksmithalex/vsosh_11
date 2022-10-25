N = int(input())
M = int(input())
if (N * (N + 1) // 2) < M:
    print(0)
else:
    while M - N > 0:
        print(N)
        M -= N
        N -= 1
    if M != 0:
        print(M)

