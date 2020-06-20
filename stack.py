a = []

print('input push or pop and number')

while True:
    c = input("input 'push' or 'pop' : ")

    if c == 'pop':
        print('pop a is', a[len(a) - 1])
        del a[len(a) - 1]
        print('show a :', a)

    elif c == 'push':
        b = int(input("input number : "))
        a.append(b)
        print('show a :', a)
