import math
'''
a = float(input('첫번째 직각변의 길이(cm) : '))
b = float(input('두번째 직각변의 길이(cm) : '))
c = math.sqrt(a**2 + b**2)
±
print('빗변의 길이는 {} cm 입니다'.format(c))
'''
'''
print('이차방정식 ax² + bx + c 해 계산기입니다.')
a = int(input('a 값 : '))
b = int(input('b 값 : '))
c = int(input('c 값 : '))
d = []

back_len = len(str(e).split('.')[1])

for i in range(back_len + 1):
    d.append('-')

d = ''.join(d)

print('\n이차방정식 {}x² + {}x + {} 의 해는 \n\n{} ± {}\n------{}\n  {}'
      .format(a, b, c, -b, e, d, 2*a))
'''

car = [['Gene'], ['Lex'], ['Infini'], ['Lambor'], ['Linc']]
print_model = []
print(car)

if str(input()) == 'list':
    while True:
        temp = str(input('\nappend = a\ndelete = d\nmodel = m\nstop = s\ninput = '))
        if temp == 's':

            print('car list is {}'.format(car))
            break
        elif temp == 'a':
            ap = str(input('append car = '))
            car.append([ap])
            print(car)
        elif temp == 'd':
            de = str(input('delete car = '))
            for i in range(len(car)):
                if car[i] == [de]:
                    print('delete car is {}'.format(de))
                    del car[i]
                    print(car)
                    break
        if temp == 'm':
            first_m = int(input('first model(number) = ')) - 1
            second_m = int(input('second model(number) = ')) - 1
            for i in range(first_m, second_m + 1):
                print_model.append(car[i])
            print(print_model)