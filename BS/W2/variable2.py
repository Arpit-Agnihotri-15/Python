ram_bank_balance = 100000
#ram's bank balance, note this is positive

ram_loan = 500000
#ram's loan, this is to be returned by him and hence will count as negative 

lakshman_bank_balance = 2000000
lakshman_loan = 1000000

net_income = (ram_bank_balance + lakshman_bank_balance) 
#net_income is the total bank balance of the two brothers.

net_liability = (ram_loan + lakshman_loan)
#net_liability is the total loan of the two brothers.

final_value = net_income - net_liability
#final_value is the family's final money (could be +ve or -ve)
print("so family has", final_value)


#We are trying to illustrate what we call the dynamic typing

a = 10
print(type(a))

a = 'India'
print(type(a))

n = 10
print(type(n))
print(n)
n = n/2
print(type(n))
print(n)

#Variable naming rules:

#1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
#2. Variable names cannot start with a number.
#3. Variable names can only contain alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
#4. Variable names are case-sensitive (e.g., age and Age are different variables).
#5. Keywords cannot be used as variable names (e.g., and, or, not, if, else, etc.)

a = 10   #can be a character
_1 = 20  #can start with underscore
a_ = 30 
A = 40
a_2 = 50  #can be mixture of char, underscore, number
_ = 60  #can be just an underscore
roll = 70
Roll = 80  #case sensitive variable name

print(a, _1, a_, A, a_2, _, roll, Roll)


#invalid variable names:

#1a = 10   #cannot start with a number
#and = 10  #cannot use keywords as variable names
#a-b = 10  #cannot use special characters like - in variable names
#1 = 10  #cannot use numbers as variable names
#@ = 10 #cannot use special character except underscore(_)

#print(1a, and, a-b, 1, @)

#The above lines are commented out because they will cause syntax errors due to invalid variable names.

#multiple assignment

x, y = 1, 2
print(x, y)
x, y = 2, 1   #ordering matters in multiple assignment
print(x, y)
x = y = z = 10 #assigning same value to multiple variables
print(x, y, z)

x, y = 1, 2
x, y = y, x  #swapping values of x and y
print(x, y)

#delete a variable
x = 10
print(x)
del x    #NameError: name 'x' is not defined
#print(x)  #this will raise an error because x has been deleted

#short hand assignment operators
count = 0
count = count + 1
count = count + 1
count = count + 1
count = count + 1
print(count)
count = 0
count += 1
count += 1
count += 1
count += 1
print(count)

count -= 1
print(count)
count *= 2
print(count)
count /= 2
print(count)

#special operators

# in  #check if a value is present in a sequence (like string, list, tuple, etc.)
print('alpha' in 'A variable name can only contain alpha-numeric characters and underscores')
print('alpha' in 'A variable name must start with a letter or the underscore character')

#chaining operators
x = 5
print(1<x<10)
print(10<x<20)
print(x<10<x*10<100)
print(10>x<=9)
print(5==x>4)

# escape characters

#print('It's a beautiful day') #this will raise an error because of the single quote in "It's"
print('It\'s a beautiful day') #using backslash to escape the single quote
#print("we are from "IIT" Madras") #this will raise an error because of the double quotes in "IIT"
print("we are from \"IIT\" Madras") #using backslash to escape the double quotes
print('My name is Arpit. \t I am from Ghaziabad. \nI am a student at IIT Madras.') #using \t for tab and \n for new line

#\t for tab(1 \t = 6 space while 1 tab = 4 spaces) and \n for new line
    
print("Hi \n I'm Arpit.") # space after \n make a space at the beginning of the new line

print("It's a beautiful day") #using double quotes to avoid the need for escaping the single quote
print('we are from "IIT" Madras') #using single quotes to avoid the need for escaping the double quotes

#use of quotes

x = 'This is a string'
y = "This is also a string"
#z = "first line 
#second line
#third line"
print(x)
print(y)
#print(z) #this will raise an error because of the new line characters in the string
z = """first line
second line
third line"""
a = '''first line
second line
third line'''   
print(z) #using triple quotes to allow for multi-line strings
print(a)

#comment 1
#comment 2
#comment 3

'''coment 1
comment 2
comment 3'''   #'''is used for multi-line comments, but it is actually a multi-line string that is not assigned to any variable, so it is ignored by the interpreter.'''