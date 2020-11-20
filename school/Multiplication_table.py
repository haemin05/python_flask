fn = int(input('first number = '))
sn = int(input('second number = '))
rg = str(input('range(press enter for 9) = '))

if rg == '':
    Rg = 9
else:
    Rg = int(rg)

for i in range(fn, sn + 1):
    for j in range(1, Rg + 1):
        print('{} x {} = {}'.format(i, j, i * j))
        if j == Rg:
            print(' ')