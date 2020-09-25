num = int(input('Enter a number'))
temp = num
s = 0
while num>0:
    rem = num % 10
    s = s +(rem*rem*rem)
    num = num//10
if s==temp:
    print('S')
else: 
    print('N')
