f = open('../../files/081223/27b_8.txt')
n = int(f.readline())
a = [int(x) for x in f]
ost = [10 ** 4 + 1] * 98
min_s = 10 ** 7
for i in range(n - 6):
    ost[a[i] % 98] = min(ost[a[i] % 98], a[i])
    if (ost[(98 - a[i + 6] % 98) % 98] + a[i + 6]) < min_s and ost[(98 - a[i + 6] % 98) % 98] != (10 ** 4 + 1):
        min_s = ost[(98 - a[i + 6] % 98) % 98] + a[i + 6]
print(min_s)
