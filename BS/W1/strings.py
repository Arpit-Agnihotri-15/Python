s = 'coffee'
t = 'bread'
print(s)
print(t)
print(s+t)

#string slicing
print(s[0])
print(s[1:5])  #str[start:end] and end at end-1
print(s[-1])  #last index

s='0123456789' #string
a = s[0]
b = s[1]
print(a)
print(b)
print(a+b) #string concatenation
a = int(a) #convert string to integer
b = int(b)
print(a)
print(b)
print(a+b) #integer addition

a = s[3]
print(type(a))
b = s[8]
n = int(a+b)
print(n)  #string concatenation and then convert to integer
print(type(n))

a = int(s[3])
print(type(a))
b = int(s[8])
n = a+b
print(n) #integer addition
print(type(n))

#replecation

s = 'good'
print(s*5)
print(s[0]*5) #replicate the first character 5 times

#string comparison

x = 'India'
print(x == 'India') 
print(x == 'india')

print('apple'>'one')
print('four'<'ten')

# comparsion  of strings is character by character and the first different character determines the result.
# The comparison is based on the ASCII values of the characters.
 
#ASCII values -> A-Z: 65-90, a-z: 97-122, 0-9: 48-57
#To find ASCII value use ord() fn. and to find charc. from ASCII value use chr() fn.

print(ord('A'))  # ASCII value of 'A'
print(ord('a'))  # ASCII value of 'a'
print(ord('0'))  # ASCII value of '0'
print(chr(65))  # Character corresponding to ASCII value 65
print(chr(97))  # Character corresponding to ASCII value 97
print(chr(48))  # Character corresponding to ASCII value 48

print('ab'<'az')
print('abcdef'<'abcde') 

#string indexing

#positive indexing:-> 0 to n-1
#negative indexing:-> -1 to -n
#n is the length of the string

s = 'python'

#positive indexing
print(s[0])  #first character
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])  #last character

#negative indexing
print(s[-1])  #last character
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])  #first character

str = 'dfbdfbdvwfjenvevwvv'
#print(s[100]) #IndexError: string index out of range

#len() fn.
#  to find the length of the string

print(len(s))
print(len(str))
#print(str[len(str)]  #IndexError: string index out of range
print(str[len(str)-1])  #last character

##PROBLEMS##

print("555""['2']") #The expression "555""['2']" is a string concatenation operation. In Python, when two string literals are placed next to each other, they are automatically concatenated. So, "555""['2']" will be evaluated as "555['2']". The output will be the combined string "555['2']".


##GRPA-5 must practice


