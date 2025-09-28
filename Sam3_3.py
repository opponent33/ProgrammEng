flag = False
num = int(input("enter the number: "))
if (num > 10) or (num < 0):
    flag = True
elif num <= 3:
    print ('number in interval(0;3]')
elif 3 < num < 6:
    print('number in interval(3;6)')
elif 6<=num <= 10:
    print('number in interval[6;10]')