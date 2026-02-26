#string methods
x = 'pytHoN sTrIng mEthOdS'
print(x.lower()) #lower case
print(x.upper()) #upper case 
print(x.capitalize()) #capitalize first letter
print(x.title()) #capitalize first letter of each word
print(x.swapcase()) #swap case
x = 'python'
y = 'Python'
print(x.islower()) #check if all characters are lower case
print(y.islower())
x = 'PYTHON'
y = 'PYTHoN'
print(x.isupper()) #check if all characters are upper case
print(y.isupper())
x = 'Python String Methods'
y = 'Python string Methods'
print(x.istitle()) #check if string is in title case
print(y.istitle())
x = '12345'
y = '123abc'
print(x.isdigit()) #check if string is a digit
print(y.isdigit())
x = 'abc'
y = 'abc123'
print(x.isalpha()) #check if string is alphabetic
print(y.isalpha())
x = 'abc123'
y = 'abc-@123'
print(x.isalnum()) #check if string is alphanumeric
print(y.isalnum())
#alpha - a-z A-Z
#digit - 0-9
x = '---pyt-hon----'
print(x.strip('-')) #remove leading and trailing characters (default is whitespace)
print(x.lstrip('-')) #remove leading characters
print(x.rstrip('-')) #remove trailing characters
print(x.strip()) #remove leading and trailing whitespace
print(x.lstrip()) #remove leading whitespace
print(x.rstrip()) #remove trailing whitespace
x = 'Python'
print(x.startswith('P')) #check if string starts with a specific substring
print(x.startswith('p'))
print(x.endswith('n')) #check if string ends with a specific substring
print(x.endswith('N'))
x = 'Python String Methods'
print(x.count('t')) #count occurrences of a substring
print(x.count('s'))
print(x.index('t')) #find the index of the first occurrence of a substring
print(x.index('s'))
x = x.replace('S', 's') #replace a substring with another substring
x = x.replace('M', 'm') #replace a substring with another substring
print(x)

#interesting cipher
alpha = 'abcdefghijklmnopqrstuvwxyz'
i = 10
print(alpha[i]) 
print(alpha[i+1])
print(alpha[i+2])
print(alpha[i+3])
print(alpha[20])
i = 100
print(i % 26) #modulo operator to wrap around the alphabet
print(alpha[i % 26])


#program to encrypt a name using the above cipher without using loop
#this os popularly known as caesar cipher, where each letter is shifted by a certain number of positions in the alphabet

alpha = 'abcdefghijklmnopqrstuvwxyz'
n = 'Arpit'
#i expect the output Bsqju, which is the name with each letter shifted by 1
cipher = ''
i = 0
k = 4   #jump of k letters
print((alpha.index(n.lower()[0]))) #index of 'A' is 0, so 0 + 1 = 1, which is 'B'
cipher += alpha[(((alpha.index(n.lower()[i]))+k)%26)]
cipher += alpha[(((alpha.index(n.lower()[i+1]))+k)%26)]
cipher += alpha[(((alpha.index(n.lower()[i+2]))+k)%26)]
cipher += alpha[(((alpha.index(n.lower()[i+3]))+k)%26)]
cipher += alpha[(((alpha.index(n.lower()[i+4]))+k)%26)]

print(cipher.capitalize())




