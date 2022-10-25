n, m = int(input()), int(input())

res = 0
while n >= 4 and m >= 4:
    k = min(n, m) // 4
    res += ((n + m) + (n + m) - 4 * (k - 1)) * k // 2
    n, m = n - 2 * k, m - 2 * k
if n == 3 and m >= 3:
    res += 2 * m + 1
elif n == 2 and m >= 2:
    res += m + 1 + int(m >= 3)
elif m == 3 and n >= 3:
    res += 2 * n + 1
elif m == 2 and n >= 2:
    res += n + 1
else:
    res += n * m
print(res)