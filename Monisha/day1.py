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


#21 Print numbers from 1 to 100.
i=1
while(i<=100):
    print(i)
    i = i+1

#22  Print all even numbers between 1 and 50.
for i in range(1,51):
    if(i%2==0):
        print(i)

#23 Calculate the factorial of a number.
n = int(input("Enter any number : "))
bag = 1
for n in range(1,n):
    n = n+1
    bag = bag*n
print(bag)

#24  Print multiplication table of any number.
n = int(input("Enter any number : "))
for i in range(1,11):
    print(n,"*", i, "=", i*n)

#25 Calculate the sum of digits of a number.
n = int(input("Enter any number : "))
total = 0
while n>0:
    digit = n%10 #get the last digit 
    total = total+digit
    n = n//10
print(total)

#26 Reverse a number.
n = int(input("Enter a number : "))
rev = 0
while(n>0):
    digit =  n%10   #get the last digit 
    rev = rev*10 + digit #reverse a number 
    n = n//10 #remove the last digit 
print(rev)

#27 Count digits in a number.
n = int(input("Enter a number : "))
count = 0
if(n==0):
    print(1)
else:
    while(n>0):
        n = n//10
        count += 1
    print(count)

#28  Print a right-angled triangle using `*`   
n = int(input("Enter any number : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()


#29 Check if a number is a palindrome.
n = int(input("Enter any number : "))
org = n
rev = 0
while (n>0):
    digit = n%10    #get the last digit 
    rev = rev*10+digit
    final = n//10
if(org == rev):
    print("number is palindrome")
else:
    print("number is not a palindrome")

#30 Check if a number is a prime number.
n = int(input("Enter a number : "))

if(n<=1):
    print("not a prime")

else:
    for i in range(2,n):
        if(n%i==0):
            print("not prime")
        else:
             print("prime")

'''
string methods 
str = "i am a software developer"
print(str.endswith("per"))
print(str.capitalize())
print(str.replace("a", "an"))
print(str.find("developer"))
print(str.count("a"))
'''

#31 Check if a string is a palindrome.
job = "Software Developer"
print(len(job))
print(job[-1:-19:-1])   #-1 in the last helps to move backwards 


#32 Count vowels in a string.
job = "Software Developer"
vowels = "aeiouAEIOU"
count = 0
for i in range(len(job)):  #i till length of job
    if job[i] in vowels:
        count+=1
print(count)

#33 Convert a string to uppercase and lowercase.
job  = "Software Developer "
print(job.lower())
print(job.upper())

#34 Replace spaces with hyphens in a string.
job = "I am a Software Developer"
print(job.replace(" ", "-"))

#35 Count the number of words in a string.
office =  "I am a Software Developer at TCS"
text = office.split()
print(len(text))

#36  Remove punctuation from a string.
job = "I am a Developer at TCS, I earn 50000 per month"
result = ""
for i in job:
    if(i!="," and i!="."):
        result+=i
print(result )

#37 Check if a word is an anagram of another.
text = "worth"
word = "throw"
text_1 = text.lower()
word_1 = word.lower()
text_2 = sorted(text_1)
word_2 = sorted(text_2)
if(text_2 == word_2):
    print("anagram")
else:
    print("not anagram")


#38 Reverse a string without using slicing.
job = "software developer"
rev = ""
for i in job:
    rev = i+rev

print(rev)

#39 Find frequency of each character.
job = "software developer"
print(job.count("a"))
    

#40  Find frequency of each character.
job = "software developer"
freq = {}
for i in job:
    if i in freq:
        freq[i] +=1

    else:
        freq[i] = 1

print(freq)
