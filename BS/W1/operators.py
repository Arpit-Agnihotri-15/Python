a = 1
b = 2
n = a + b  # Addition of two numbers using +
print(n)

p = 'Arpit'
q = 'Agnihotri'
m = p + q  # Concatenation of strings using +
print(m)

r = [1,2,3]
s = [4,5,6]
t = r + s  # union of two lists using +
print(t)  

u = 10+13*2
# my guess is u will be 46.
#the expected answer was incorrect, the correct answer turns out to be 36, this is due to what is called the operator precedence.
print(u)
v = ((10+13)*2)
print(v) #the expected answer is 46, and it turns out to be correct. This is because the parentheses have the highest precedence, so the addition is performed first, followed by the multiplication.
#
#OPERATORS
#
#Arithmetic Operators: +, -, *, /, //, %, **
#
a = 10
b = 3
print('a:', a)
print('b:', b)
#
print('Arithmetic Operators:')
print('Addition:',a,'+',b,'=', a + b)  # Addition
print('Subtraction:',a,'-',b,'=', a - b)  # Subtraction
print('Multiplication:',a,'*',b,'=', a * b)  # Multiplication
print('Division:',a,'/',b,'=', a / b)  # Division
x = int(input())
y = int(input())
z = int(input())
avg = (x + y + z) / 3
print(avg)  #division operation always results in a float.
#
print('Floor Division:',a,'//',b,'=', a // b)  # Floor Division
#Difference between / and // is that / gives the quotient as a float, while // gives the quotient as an integer (floor value).
#
print('Modulus:',a,'%',b,'=', a % b)  # Modulus
#The modulus operator (%) gives the remainder of the division of a by b. In this case, 10 divided by 3 gives a quotient of 3 with a remainder of 1, so a % b evaluates to 1.
#
print('Exponentiation:',a,'**',b,'=', a ** b)  # Exponentiation
print(2 ** 3 ** 0) #The expression 2 ** 3 ** 0 is evaluated as follows:
#1. The exponentiation operator (**) is right-associative, which means that it is evaluated from right to left.
#2. The expression 3 ** 0 is evaluated first, which gives 1 (since any number raised to the power of 0 is 1).
#3. Then, the expression 2 ** 1 is evaluated, which gives 2.
#
#Relational Operators: ==, !=, >, <, >=, <=
print('relational operators:')
#gives output in boolean values, either true or false.
#
print('Equal to:',a,'==',b,'=', a == b) #equality operator
print('Not equal to:',a,'!=',b,'=', a != b) #inequality operator
print('Greater than:',a,'>',b,'=', a > b) #greater than operator
print('Less than:',a,'<',b,'=', a < b) #less than operator
#
print('Greater than or equal to:',a,'>=',b,'=', a >= b) #greater than or equal to operator
#difference between > and >= is that > checks if a is strictly greater than b, while >= checks if a is greater than or equal to b. In this case, since 10 is greater than 3, both a > b and a >= b will evaluate to True.
#
print('Less than or equal to:',a,'<=',b,'=', a <= b) #less than or equal to operator
#difference between < and <= is that < checks if a is strictly less than b, while <= checks if a is less than or equal to b. In this case, since 10 is not less than 3, both a < b and a <= b will evaluate to False.
#
#Logical Operators: and, or, not
print('Logical Operators:')
#
c = True
d = False
print('c:', c)
print('d:', d)
#
print('c and c:', c and c) #and operator
print('c and d:', c and d)
print('d and c:', d and c)
print('d and d:', d and d)
#The and operator returns True if both operands are True, otherwise it returns False. In the above examples, only the first case (True and True) evaluates to True, while the other three cases evaluate to False.
#
print('c or c:', c or c) #or operator
print('c or d:', c or d)
print('d or c:', d or c)
print('d or d:', d or d)
#The or operator returns True if at least one of the operands is True, otherwise it returns False. In the above examples, the first three cases (True or True, True or False, False or True) evaluate to True, while the last case (False or False) evaluates to False.
#
print('not c:', not c) #not operator
print('not d:', not d)
#The not operator returns the opposite of the operand. In the above examples, not True evaluates to False, and not False evaluates to True.

##PROBLEMS##

print(5 and 2) #The expression 5 and 2 evaluates to 2. In Python, the and operator returns the first operand if it is falsy (e.g., False, 0, empty string), otherwise it returns the second operand. Since 5 is a non-zero integer (which is considered truthy), the expression evaluates to the second operand, which is 2.

# print('5' * 2.0)
#The expression '5' * 2.0 results in a TypeError. In Python, the multiplication operator (*) can be used to repeat a string a certain number of times when the second operand is an integer. However, when the second operand is a float (like 2.0), it is not valid for string repetition, and thus Python raises a TypeError indicating that the operands are of incompatible types.

print(5 == 5 and "2") #The expression 5 == 5 and "2" evaluates to "2". In Python, the and operator returns the first operand if it is falsy (e.g., False, 0, empty string), otherwise it returns the second operand. Since 5 == 5 evaluates to True (which is considered truthy), the expression evaluates to the second operand, which is the string "2".

m = a == b > c == d
n = (a == b) and (b > c) and (c == d)
print(m == n) #The expression ((a == b) and (b > c) and (c == d))==((a == b) and (b > c) and (c == d)) evaluates to True. This is because both sides of the equality operator (==) are identical expressions, so they will always evaluate to the same boolean value. Therefore, the overall expression will always be True regardless of the values of a, b, c, and d.