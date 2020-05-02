#test login

a = input('id : ')
b = input('password : ')

id = ['haemin', 'system', 's_deo']
password = ['1234', '7412', '0117']
flag = 0

for i in range(len(id)):
    if a == id[i] and b == password[i]:
        print('login!')
        flag = 1

if flag == 0:
    print('try again')
