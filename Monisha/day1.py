#1 Print "Hello, World!"
print("Hello, World!")

#2 Assign your name to a variable and print it.
name = "Monisha Mondal"
print(name)

#3 Store age in a variable and print it.
age = 22
print(age)

#4 Swap two numbers using a third variable.
a = 36
b = 45
c = a 
a = b 
b = c

print(a,b)


#5 Swap two numbers without using a third variable.
a = 10
b = 5

print("a = ", b)
print("b = ",a)

#6  Take name as input and greet the user.
greet = input("Enter any name : ")
print(f"Good morning {name}")

#7 Input two numbers and print their sum.
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
sum = a + b
print(sum)

#8 Input a number and check if it's positive, negative, or zero.
number =  int(input("Enter any number : "))
if(number ==0):
    print("Number is zero")
elif(number>=0):
    print("Positive Number")
else:
    print("Negative Number ")


#9. Convert temperature from Celsius to Fahrenheit.
C = int(input("Enter temperature in Celsius "))
temp = (C*9/5)+32
print(temp )

#10 Take user input of 3 subjects and print their average.
maths = int(input("Enter your maths marks : "))
science = int(input("Enter your science marks : "))
social = int(input("Enter your social marks : "))
avg =(maths+science+social)/3
print(avg)

#11 Find the remainder when one number is divided by another.
divisor = int(input("Enter any number : "))
dividend = int(input("Enter any number : "))
remainder = divisor/dividend
print("remainder is : ", remainder)

#12 Check if a number is even or odd.
number = int(input("Enter any number : "))
if(number%2==0):
    print("even no.")
else:
    print("odd no.")

#13 Use logical operators to check if a number lies between 10 and 50.
number = int(input("Enter any number : "))
if(10<=number<=50):
    print("number lies between 10 and 50 ")
else:
    print("number does not lie between 10 and 50 ")

#14 Calculate compound interest.
p = int(input("Enter principal : "))
t = int(input("Enter time : "))
r = int(input("Enter rate : "))
n = int(input("Compounded per year : "))
Amount = p*(1+r/n)**(n*t)
print("Compund interest is : ", Amount)

#15 Write a program to find square and cube of a number.
n = int(input("Enter any number : "))
square = n**2
cube = n**3
print("sqaure of the number is : ",square)
print("cube of the number is : ",cube)

#16  Check if a year is a leap year.
year = int(input("Enter any year : "))
if(year%4==0):
    print("Leap year")
else:
    print("Not a leap year")


#17  Find the greatest of three numbers.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))
if(n1>n2 and n1>n3):
    print(n1,"is greater")
elif(n2>n1 and n2>n3):
    print(n2, "is greater")
else:
    print(n3, "is greater")

#18 Write a calculator using `if-elif-else`.
n1 = int(input("Enter first number : "))
operator = input("Enter any operator : ")
n2 = int(input("Enter second number : "))
if(operator == "+"):
    sum = n1+n2
    print("sum of two numbers is : ", sum)
elif(operator == "-"):
    sub = n1-n2
    print("sub of two numbers is : ", sub)
elif(operator == "*"):
    multi = n1*n2
    print("multiplication of two numbers is : ", multi)
elif(operator == "/"):
    division = n1/n2
    print("division of two numbers is : ", division)
else:
    print("Please enter operator between (+, =, /, *)")


#19 Check if a number is divisible by both 5 and 7.
number =  int(input("Enter any number : "))
if(number%5==0 and number%7==0):
    print("number is divisible by both 5 and 7 ")
else:
    print("number is not divisible by both 5 and 7 ")

#20 Categorize age into child, teen, adult, senior.
age  =  int(input("Enter the age : "))
if(age>1 and age<=12):
    print("person is child ")
elif(age>=13 and age<18):
    print("person is teen ")
elif(age>=18 and age>=30):
    print("person is adult")
elif(age>30):
    print("person is a senior citizen")
else:
    print("Enter a valid age ")