N = int(input())
M = int(input())

p = (lambda a, b: ((a // b) * a + (b // a) * b) // (a // b + b // a))(N, M)
q = p  - (N + M - p - 1) // 2 * 2
r = 2 - (N + M - p) % 2

print(q * r)