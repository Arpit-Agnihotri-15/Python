print("Hello India")
print('Hello World')
print("Hello India",'Hello World',"Hi python")
print(10)
print(20.50)
print("Hello India", 10, 20.50)

#common mistakes while using print function

#spelling mistake
#prnt("Hello India")   --> NameError: name 'prnt' is not defined

#missing parenthesis
#print "Hello India"  --> SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello India")?

#wrong brackets
#print["Hello India"]  --> TypeError: 'builtin_function_or_method' object is not subscriptable
#print<"Hello India">  --> SyntaxError: invalid syntax

#missing quotes
#print(Hello India)  --> NameError: name 'Hello' is not defined

#python is flexible with quotes
print('Hello India')
print("Hello India")

#start with single quote so end with single quote and vice versa
#print('Hello "India")  --> SyntaxError: EOL while scanning string literal
#print("Hello 'India")  --> SyntaxError: EOL while scanning string literal

##PROBLEMS##

#print is a function and not a keyword, so it can be used as a variable name, but it is not recommended as it can lead to confusion and errors in the code. For example:
#print() prints space between multiple values
#print() can be used to display and data type

#input is also not a keyword, but a built-in function
#output type of input is always string, so we need to convert it to the desired data type using int(), float(), etc. functions.
