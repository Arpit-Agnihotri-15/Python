print(10)
a = 10        #variable 'a' which is stored with value = 10
print(a)
b = 20        #variable 'b'
print(b)
print(a+b)
print(a*b)
a = a+1       #variable a is assigned to sum of previous value stored in 'a' with 1
print(a)
a = a+1
print(a)
a = a+1
print(a)

#Input from user

#input() function is used to take input from user and it returns a string value. So, we need to convert the input into integer using int() function.

#integer input

print("Enter a number :")
num = int(input())   
print(num)
print(num+1)
print(num*2)

#string input

print("Hello, what is your name?")
name = str(input())
print(name)
print("hello", name, "welcome to python programming")

print("Which place are you in?")
place = str(input())
print("You are in", place, "and your name is", name, ".")

age = int(input("How old are you? ")) #merge print and input function
print("Good to Know that you are", age, "years old.")

#variable are just like a box where we can store any value and we can use that value later in our program. We can change the value of variable at any time in our program.

name = "Alice"
name = "Bob"  #variable name is assigned to new value "Bob"
name = "Charlie" #variable name is assigned to new value "Charlie"
print(name) #output will be "Charlie" because the last value assigned to variable name is "Charlie"

age = 25
age = 30
age = age + 5  # Update age to a new value
print(age)

#35 = 35+1
#This will give an error because we cannot assign a value to a number. We can only assign a value to a variable.

#this concludes that literals (like numbers and strings) cannot be assigned a value, only variables can be assigned a value.
#literals can be used only on the right side of an assignment operator, whereas variables can be used on both sides of an assignment operator.

#when to use variables? and when to use literals?

r = int(input("Enter the radius of the circle: "))
area = 3.14 * r * r  
#r is a variable which is used to store the value of radius and it is used in the formula to calculate the area of the circle. 
#3.14 is a literal which is used as a constant value in the formula to calculate the area of the circle. We cannot change the value of 3.14, but we can change the value of r.
#by changing r the value of area also changes which is also a variable
print("The area of the circle with radius", r, "is", area)

#so variables are used when there is a possibility of change in value and literals are used when there is a constant value which does not change.