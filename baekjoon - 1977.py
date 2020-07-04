m = 60
n = 100
num = 1
plus = 0
small_num = []

while True:
    if num * num >= m:
        plus += (num * num)
        small_num.append(num * num)
    if num * num > n:
        break
    num += 1
    print("num", num)

print(plus, small_num[0])