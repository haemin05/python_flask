'''
l = input()
a = []

temp = l.split(' ')

for i in range(len(temp)):
    if temp[i] != '':
        a.append(temp[i])

print(len(a))
'''

n = int(input('card : '))
d = int(input('goal : '))
num = []
save = []

print('')
for i in range(1, n + 1):
    N = int(input('card{} : '.format(i)))
    num.append(N)

#for j in range(1, 3+1):
#    sun = int(input('goal card {}').format(j))

for a in range(len(num)):
    for b in range(len(num) - 1):
        for c in range(len(num) - 2):
            if (num[a] + num[b+1] + num[c+2] == d) or (num[a] + num[b+1] + num[c+2] <= d):
                save.append(num[a] + num[b+1] + num[c+2] - d)

save.sort()
print(save)