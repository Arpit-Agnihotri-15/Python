n = 10
print(n)
r = 3.14
print(r)
s = "Arpit"
print(s)

print("n is of type:", type(n))
print("r is of type:", type(r))
print("s is of type:", type(s))

l = [1, 2, 3, 4, 5] 
print(l)
print(l[0])  # Accessing the first element of the list
#counting of elements starts from 0
print(l[1])
print(l[2])
print(l[3])
print("l is of type:", type(l))
print(l[4])
print("Type of l[4] i.e.", l[4], "is:", type(l[4]))

b1 = True
b2 = False
print("type(b1)",b1,"is:", type(b1))
print("type(b2)",b2,"is:", type(b2))

#conversion of data types

#conversion to int

a = int(3.14)  # converting float to int
print("a is:", a, "and type of a is:", type(a))  # Note: only the integer part is retained, the decimal part is truncated
b = int('123')  # converting string to int
print("b is:", b, "and type of b is:", type(b))

#conversion to float

c = float(10)  # converting int to float
print("c is:", c, "and type of c is:", type(c))
d = float('456')  # converting string to float
print("d is:", d, "and type of d is:", type(d))

#conversion to string

e = str(23) # converting int to string
print("e is:", e, "and type of e is:", type(e))
f = str(3.14) # converting float to string
print("f is:", f, "and type of f is:", type(f))

#conversion to boolean 
    
#all non-zero numbers are considered True, while zero is considered False
g = bool(10)  # converting int to boolean
print("g is:", g, "and type of g is:", type(g))  #
h = bool(0)  # converting int to boolean
print("h is:", h, "and type of h is:", type(h))  #
i = bool(-10)  # converting int to boolean
print("i is:", i, "and type of i is:", type(i))  #

#all non-zero floats are considered True, while zero is considered False
j = bool(3.14)  # converting float to boolean
print("j is:", j, "and type of j is:", type(j))  #
k = bool(0.0)  # converting float to boolean
print("k is:", k, "and type of k is:", type(k))  #
l = bool(-3.14)  # converting float to boolean
print("l is:", l, "and type of l is:", type(l))  #

#all non-empty strings are considered True, while empty strings are considered False
m = bool("")  # converting empty string to boolean
print("m is:", m, "and type of m is:", type(m))  # 
n = bool("Hello")  # converting non-empty string to boolean
print("n is:", n, "and type of n is:", type(n))  # 
o = bool(" ")  # converting string with space to boolean
print("o is:", o, "and type of o is:", type(o))  #
p = bool('10') # converting string with number to boolean
print("p is:", p, "and type of p is:", type(p))  #
q = bool('0') # converting string with number to boolean
print("q is:", q, "and type of q is:", type(q))  #

#False and None are considered False in boolean context, while True is considered True
r = bool(True) # converting boolean True to boolean
print("r is:", r, "and type of r is:", type(r))  #
s = bool(False) # converting boolean False to boolean
print("s is:", s, "and type of s is:", type(s))  #
t = bool(None) # converting None to boolean
print("t is:", t, "and type of t is:", type(t))  #

#Note: In Python, the following values are considered False in a boolean context: None, False, 0 (zero of any numeric type), 0.0 (zero float), 0j (zero complex), empty sequences (e.g., '', (), []), and empty mappings (e.g., {}). All other values are considered True.

##PROBLEMS##

print(type(13 % 5 // 2 * 30 ** 5))
print(type("@Python"))
print(type(20 ** 10 / 2 + 25 - 70))
print(type((5 > 3) and False))
print(type(20 * 100.0 // 11 % 5))
print(10//5, 10.4//5, 10//5.0)

# // is the floor division operator, which performs division and returns the largest integer less than or equal to the result. It can be used with both integers and floats. When used with integers, it returns an integer result, and when used with floats, it returns a float result.