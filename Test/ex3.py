a = list(map(int, input().split()))
n = a[0]
for i in range(1, n + 1):
    x, nr = a[i], 0
    while x > 0:
        nr = nr * 100 + x % 10
        x //= 100
    while nr > 0:
        x = x * 10 + nr % 10
        nr //= 10
    print(x)