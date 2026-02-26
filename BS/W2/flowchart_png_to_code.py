print("Travel from City A to City B")
Time = int(input('Enter time: '))
Longer = int(input('Define Longer: '))
if(Time >= Longer):
    Price = int(input('Enter Price: '))
    Higher = int(input('Define higher: '))
    if(Price >= Higher):
        print('Train')
    else:
        print('coach')
else:
    Price = int(input("Enter Price: "))
    Higher = int(input('Define higher: '))
    if(Price >= Higher):
        print('Train')
    else:
        print('coach')
print('Arrived City B')
