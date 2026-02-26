#method 1:
marks = int(input("Enter the marks: "))
if(marks < 0 or marks > 100):   # marks < 0 or marks > 100
    print("Invalid marks")
elif (marks >= 90 and marks <= 100):     # marks >= 90 and marks <= 100
    print("Grade A")
elif (marks >= 80):   # marks >= 80 and marks < 90
    print("Grade B")
elif (marks >= 70):   # marks >= 70 and marks < 80
    print("Grade C")
elif (marks >= 60):   # marks >= 60 and marks < 70
    print("Grade D")
else:               # marks < 60
    print("Grade E")
                       
#In if-elif chains:
#Always handle invalid or edge cases first

#method 2:
marks = int(input("Enter the marks: "))
if (marks >= 0 and marks <= 100):
    if (marks >= 90):
        print("Grade A")
    elif (marks >= 80):
        print("Grade B")
    elif (marks >= 70):
        print("Grade C")
    elif (marks >= 60):
        print("Grade D")
    else:
        print("Grade E")
else:
    print("Invalid marks")