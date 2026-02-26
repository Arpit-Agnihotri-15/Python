#method 1 ****
num = int(input("Enter a number: "))
if( (num % 2 == 0) and (num % 5 == 0) ):
    print('0')
elif(num % 5 == 0):
    print('5')
else:
    print('other')

#method 2 ***
num = int(input("Enter a number: "))
if(num % 5 == 0):
    if(num % 10 == 0):
        print('0')
    else:
        print('5')
else:
    print('other')

#method 3 *****
num = int(input("Enter a number: "))
if(num % 10 == 0):
    print('0')
elif(num % 5 == 0):
    print('5')
else:
    print('other')

#method 4 ****
num = int(input("Enter a number: "))
if(num % 5 == 0):
    if(num % 2 == 0):
        print('0')
    else:
        print('5')
else:
    print('other')
