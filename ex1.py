f = open('../../files/081223/27b_1.txt')
n = int(f.readline())
a = [int(x) for x in f]
ost = [0 for i in range(210)]
r = 0
for i in range(n - 7):
    ost[a[i] % 210] += 1
    r += ost[(210 - a[i + 7] % 210) % 210]
print(r)
