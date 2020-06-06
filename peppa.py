a = input()
b = []
c = []
d = 0
e = 1

f = a.split('!')
num = int(f[0])

for i in range(len(a)):
    if a[i] == '!':
        c.append(a[i])
d = len(c)

for j in range(num):
    if num - (j * d) > 0:
        e = e * (num - (j * d))
print(e)