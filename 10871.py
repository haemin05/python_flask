import random
X = [10, 5]
N = []
P = []
for n in range(X[0]):
    N.append(random.randrange(1, 10+1))

print("N is", N)

for i in range(len(N)):
    if N[i] < X[1]:
        P.append(N[i])
print(P)