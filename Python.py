# Simple if conditional/Decisional statement -------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# WAP to check whether the JOb location is banglore or not

# Job_location = input("Enter Your job Location : ")
# if Job_location == 'banglore':
#     print("True")

# WAP to check whether the enter character is vowels or not

# char = input("Enter your character : ")

# # if char == "a" or char == "e" or char == "o" or char == "i" or char == "u" or char == "A" or char == "E" or char == "O" or char == "I" or char == "U":
# #     print("Your enter character is a vowel")

# a = ["a","e","i","o","u","A","E","I","O","U"]
# if char in a:
#     print("Your enter a vowel") 

# check whether a number is even or not
# num =int(input("Enter a number: "))
# if num % 2 == 0:
#     print("number is even")
    
# check whether a number is odd or not
# num =int(input("Enter a number: "))
# if num % 2 != 0:
#     print("number is odd")

#WAP to check whether the number is even or or not and if its even check it is multiple or 4 or not
# num =int(input("Enter a number: "))
# if num % 2 == 0 and num % 4 == 0:
#     print("number is even and divisible by 4")

    
# num =int(input("Enter a number: "))
# if num % 2 == 0 or num % 5 == 0:
#     print("number is even or multiple by 5")

# WAP to check whether the entered char is uppercase or not

# char = input("Enter a char : ")
# uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"    
# if char in uppercase:
#     print("Entered char is uppercase")

# # WAP to check length of the string

# string = input("Enter a string : ")
# if type(string) == str:
#     print(len(string))

# a = input("Enter a value : ")
# if type(string) == str:
#     print(len(string))

# WAP to check 
# a = input("Enter a value : ")
# if len(a)== 1:
#     print("The input is a character")

# if-else conditional/Decisional statement ---------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# mutuable = LSD = List, Set, Dict

# WAP to check the given data type is immutable or mutuable data type or not

# a = eval(input('Enter the data : '))
# if type(a) in (list, set, dict):
#     print("mutuable data type")
# else:
#     print("immutable data type")

# WAP to check whether the entered data is single valued data type / multi valued datatype or not

# a = eval(input('Enter the data : '))
# if type(a) in (int, float, complex, bool):
#     print("single valued data type")
# else:
#     print("multi valued data type")

# WAP to check whether the given string is having middle char or not

# a = input("Enter a value : ")
# if len(a) % 2 == 0:
#     print("middle char is not present")
# else:
#     print("it does has middle char")

# WAP to check whether the first value inside the list is integer or not

# a = [1,"hii", "hello",2]

# if type(a[0]) == int:
#     print(" the first value is integer ")
# else:
#     print("the first value is not integer")

# WAP to check whether the entered char is special char or not

# a = input("Enter a char : ")

# if a in "~`!@#$%^&*()_+=-;'""/.,<>?":       # method-1
#     print("enter char is a special char")
# else:
#     print("Entered char is not a special char")

# if ("A"<=a<="Z" or "a"<=a<="z" or "0"<=a<="9"):     # method-2
#     print("not a special char")
# else:
#     print("special char")

# WAP ro check whether the no. is even or odd if the no. is even print square of the no., if its odd print cube of the no.

# a = int(input("Enter a number : "))
# if a % 2 == 0:
#     b = a**2
#     print("the number is even and its square is : ",b)
# else:
#     c = a**3
#     print("the number is odd and its cube is : ",c)

# WAP to check whether the entered char alphabet or not

# a = input("Enter a char : ")

# if ("A"<=a<="Z" or "a"<=a<="z"):
#     print("The entered char is a alphabet")
# else:
#     print("The entered char is not a alphabet")

# WAP to take 2 values inside a list and check whether list is homo or hetro or not

# a = eval(input("Enter a list : "))

# if type(a[0]) == type(a[1]):
#     print("It is homegeneous list")
# else:
#     print("Its a hetrogeneous list")

# check whether the last char in the list is int or not
# a = ["h","a",2]
# if type(a[-1]) == int:
#     print("int")
# else:
#     print("not int")

# WAP to check whether the 2 values are pointing towards same memory location or not

# a=10
# b=20
# if a is b:
#     print("both the values arre pointing to same memory location")
# else:
#     print("both the values are pointing towards different memory location")

# WAP to to check whether the given string is palindrome or not

# a = input("Enter a string : ")
# if a[::1] == a[::-1]:
#     print("the entered string is a palindrome")
# else:
#     print("Entered string is not a palindrome")

# WAP to print reverse of the string only if the length is greater than 5 or else print the string is as it is

# a = input("Enter a string : ")

# if len(a)>5:
#     print(a[::-1])
# else:
#     print(a)

# elif ------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# it is a conditional statement which is used whenever we have more than one condition and each condition will have statement block.

# 1.) WAP to check whether the entered char is uppercase, lowercase, integer if its a integer print ascii value of it

# a = input("Enter a value : ")

# if ("A"<=a<="Z"):
#     print("Uppercase",a)
# elif ("a"<=a<="z"):
#     print("Lowercase",a)
# elif ("0"<=a<="9"):
#     print("its number",a,"and its ascii value is : ",ord(a))
# else:
#     print(f"{a} is a special char")

# 2.) WAP to find the entered data is indiviual data type or collection datatype

# a = eval(input("Enter a value : "))

# if type(a) == int:
#     print(f"{a} is a single value datatype")
# elif type(a) == float:
#     print(f"{a} is a single value datatype")
# elif type(a) == complex:
#     print(f"{a} is a single value datatype")
# elif type(a) == bool:
#     print(f"{a} is a single value datatype")
# else:
#     print(f"{a} is a multi value datatype")

# 3.) WAP to find highest of 2 numbers

# a = int(input("Enter a number : "))
# b = int(input("Enter another number : "))

# if a>b:
#     print(f"{a} is greater than {b}")
# elif b>a:
#     print(f"{b} is greater than {a}")
# else:
#     print(f"both {a} and {b} are equal")

# 4.) WAP to find highest of 3 numbers

# a = int(input("Enter 1st number : "))
# b = int(input("Enter 2nd number : "))
# c = int(input("Enter 3rd number : "))


# if a>b and a>c:
#     print(a,">",b,c)
# elif b>a and b>c:
#     print(b,">",a,c)
# elif c>a and c>b:
#     print(c,">",a,b)
# elif a==b and a>c:
#     print(f"{a}={b} and {a}>{c}")
# elif a==b and a<c:
#     print(f"{a}={b} and {a}<{c}")
# elif a==c and a>b:
#     print(f"{a}={c} and {a}>{b}")
# elif a==c and a<b:
#     print(f"{a}={c} and {a}<{b}")
# elif b==c and b>a:
#     print(f"{c}={b} and {b}>{a}")
# elif b==c and b<a:
#     print(f"{c}={b} and {b}<{a}")
# elif c==b and c>a:
#     print(f"{c}={b} and {c}>{a}")
# elif c==b and c<a:
#     print(f"{c}={b} and {c}<{a}")

# 5.) WAP to check whether the entered char is uppercase or lowercase, if the entered char is uppercase convert to lowercase and viceversa and for numbers print ascii value

# a = input("enter a value : ")

# if ("A"<=a<="Z"):
#     print(chr(ord(a)+32))
# elif ("a"<=a<="z"):
#     print(chr(ord(a)-32))
# elif ("0"<=a<="9"):
#     print("its a number and its ascii value is",ord(a))
# else:
#     print("its a special char")

# 6.) FIZZ-BUZZ program

# a = int(input("Enter a number : "))

# if a%7==0 and a%5==0:
#     print("FIZZ - BUZZ")
# elif a%5==0:
#     print("BUZZ")
# elif a%7==0:
#     print("FIZZ")

# 7.) find the length of a number

# a = int(input("Enter a value : "))
# print(len(str(a)))

# if len(str(a))==1:
#     print("length is 1")
# elif len(str(a))==2:
#     print("length is 2")
# elif len(str(a))==3:
#     print("length is 3")
# elif len(str(a))==4:
#     print("length is 4")
                            # b=str(a)
                            # count = 0
                            # for i in range(0,len(b)):
                            #     count+=1
                            # print(f"the length of the {a} is {count}")

# find middle value of a list

# a = ["siddhi", "dhrushti", "sakshi", "tanishq", "soham"]
# # print(a[len(a)//2])
# if len(a)%2!=0:
#     b=len(a)//2
#     print(a[b])


# Nested if ------------------------------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# A if condition inside another if condition is nothing but nested if.
# Here multiple condition and multiple statement blocks will be there.

# 1.) WAP to login into instagram

# user_input = input("Enter your username : ")
# password_input = input("Enter your password : ")

# username = "Harsh"
# password = "@saroja123"

# if user_input == username:
#     if password_input == password:
#         print("Login Successfull")
#     else:
#         print("Invalid password")
# else:
#     print("Invalid Username")


# 2.) less than 35 fail
# 35-60 2nd class pass
# greater than 60 than 1st class pass

# marks = int(input("Enter your percentage : "))

# if 35<=marks<=60:
#     print("2nd class pass")
# elif marks > 60:
#     print("1st class pass")
# else:
#     print("Fail")

# 3.) How to check if given char is vowel or not:

# a = input("Enter a char : ")

# if type(a)==str:
#     if a in 'AEIOUaeiou':
#         print("Its a vowel")
#     else:
#         print("Its not a vowel")
# else:
#     print("Its not a string data type")

# 4.) WAP to fetch the middle value inside a list only if its a string and print the string

# a = ["h","a","r","s","h"]

# if len(a)%2 == 1:
#     if type(a[len(a)%2]) == str:
#         print(a[len(a)//2])
#     else:
#         print("Its not a string")
# else:
#     print("Its a even  list")

# take a tuple find last value if its string reverse it only if the first char is vowel

# tup= ("harsh","gupta", "vishu", "kunal", "amukulp")

# if type(tup[-1]) == str:
#     if tup[-1][0] in "AEIOUaeiou":
#         print(tup[-1][::-1])
#     else:
#         print("Its not a vowel")
# else:
#     print("Its not a string")

# find the highest value among 3 numbers

# a, b, c = 10 , 20 , 30

# if a>b and a>c:
    
#     if b>c:
#         print("b>c")
#     else:
#         print("c>b")
# else:
#     print("a is greater")
    
# # find the highest  among the 4 numbers

# a,b,c,d = 10,5,40,90

# if a>b:
#     if a>c:
#         if a>d:
#             print("a is greater")
#         else:
#             print("d is greater")
#     else:
#         print("c is greater")
# else:
#     if b>c:
#         if b>a:
#             if b>d:
#                 print("b is greater")
#             else:
#                 print("d is greater")
#         else:
#             print("a is greater")
#     else:
#         print("c is greater")

# highest among the 4 number when any 2 numbers are equal

# a,b,c,d = 10,100,80,100

# if a>b or (a is b):
#     if a>c or (a is c):
#         if a>d or (a is d):
#             print("a >= d")
#         else:
#             print("d is not greater or equal to d")
#     else:
#         print("c is not greater or equal")
# else:
#     if b>c or (b is c):
#         if b>d or (b is d):
#             print("b is not greater or equal to d")
#         else:
#             print("")
#     else:
#         print("")

#WAP to to find the lowest of 3 numbers

# a,b,c = 100,200,30

# if a<b:
#     if a<c:
#         print("a is smallest")
#     else:
#         print("c is smallest")
# else:
#     if b<c:
#         print("b is smallest")

# find the 2nd highest number out of 4 numbers

# a,b,c,d = 10,20,30,40

# if a>b and a>c and a>d:
#     if b>c and b>d:
#         print("b is 2nd")
#     elif c>d and c>b:
#         print("c is 2nd")
#     elif d>c and d>b:
#         print("d is 2nd")
#     else:
#         print("2 numbers are identical")
# elif b>a and b>d and b>c:
#     if a>c and a>d:
#         print("a is 2nd")
#     elif c>d and c>b:
#         print("c is 2nd")
#     elif d>c and d>b:
#         print("d is 2nd")
#     else:
#         print("2 numbers are identical")
# elif c>a and c>d and c>b:
#     if a>b and a>d:
#         print("a is 2nd")
#     elif b>d and b>a:
#         print("b is 2nd")
#     elif d>b and d>a:
#         print("d is 2nd")
#     else:
#         print("2 numbers are identical")
# elif d>a and d>c and d>b:
#     if a>b and a>c:
#         print("a is 2nd")
#     elif b>c and b>a:
#         print("b is 2nd")
#     elif c>b and c>a:
#         print("c is 2nd")
#     else:
#         print("2 numbers are identical")



# user_drink = input("Which drink do you want : ")

# if user_drink == "beer":
#     print("i have beer")
# elif user_drink == "whisky":
#     print("i have whisky")
# elif user_drink == "rum":
#     print("i have rum")
# elif user_drink == "pepsi":
#     print("i have pepsi")
# else:
#     print("i don't have any thing you can go")

# -------------------------------------------------------__LOOPING STATEMENT__-----------------------------------------------------------------------------------

# looping statement:
#                   looping is nothing but set of instruction repeated continously until the condition is false.

# there are 2 types of loops:
#                           1.) while loop
#                           2.) For loop

# 1.) While loop:
# Its a looping statement where a set of instruction will repeat continously until the given condition is failing

# SYNTAX :
#           initialization
#           while <cond>:
#               statement block
#                   updation

# If we forget to initailize the looping variable, it will throw error.
# If we forget to update the looping variable, infinite loop will occur.



#                                                   *************__WHILE LOOP PROGRAM__**************

# WAP to print Harsh for 5 times

# i=0
# while i<5:
#     print("Harsh")
#     i+=1

# WAP to print natural numbers

# natural = int(input("Enter a number : "))
# i=1
# while i <= natural:
#     print(i)
#     i += 1

# WAP to print multiplication of tables

# mul = int(input("Enter which number table do you want : "))
# i = 1
# while i<11:
#     print(mul,"*",i,"=",mul*i)
#     i += 1

# WAP to extract the numbers which are divisible by 5 from 1 to 100

# i=1
# while i<101:
#     if i%5==0:
#         print(i)
#     i+=1

# WAP to extract all the uppercase char from a string

# User = input("Enter the string : ")
# i = 0
# while i<len(User):
#     if "A"<=User[i]<="Z":
#         print(User[i])
#     i+=1

# WAP to extract special char from string

# user = input("Enter your String: ")
# list = []
# i=0
# a="`!@#$%^&*()_=+][}{';:?><,./"
# while i<len(user):
#     if user[i] in a:
#         # print(user[i])
#         list.append(user[i])
#     i += 1
# print(list)

# WAP to extract all the int value present inside a list

# user = eval(input("Enter a list: "))

# i = 0
# out = []
# while i<len(user):
#     if type(user[i]) == int :
#         out.append(user[i])
#     i+=1
# print(out)

# WAP to print sum natural numbers

# natural = int(input("Enter a number : "))
# sum = 0
# i=1
# while i <= natural:
#     # print(i)
#     sum += i
#     i += 1
# print(sum)

# WAP to extract all the even index values from a tuple

# a = (1,"harsh",3,8,45,48,4,5)
# even = ()
# i=0
# while i<len(a):
#     if i%2==0:
#         even = even + (a[i],)
#         print(a[i])
#     i+=1
# print(even)

# find the factorial of a number

# num = int(input("Enter a number : "))
# i=1
# mul=1
# while i<num+1:
#     mul = mul * i
#     i+=1
# print(mul)

# WAP to add all the int values present in the tuple

# a = (1,"harsh",3,8)
# sum = 0
# i=0
# while i<len(a):
#     if type(a[i]) == int:
#         sum = sum + a[i]
#     i+=1
# print(sum)

# WAP to extract all the string values in a list only if the len is greater than 3

# a = ["harsh","gupta","mukul","vishu","raj","kunal","ram"]
# out = []
# i=0
# while i<len(a):
#     if type(a[i]) == str and len(a[i])>3:
#         out.append(a[i])
#     i+=1
# print(out)

# WAP to extract uppercase, lowercase and number in a string

# a = "HarshGupta@123"
# i=0
# str = ""
# while i<len(a):
#     if "A"<=a[i]<="Z" or "a"<=a[i]<="z" or "0"<=a[i]<="9":
#         print(a[i])
#         str += a[i]
#     i+=1

# print(str)

#WAP to toggle the string

# a = "HarshGupta"
# i=0
# new_str=''
# while i<len(a):
#     if ("A"<=a[i]<="Z"):
#         new_str+=chr(ord(a[i])+32)
#     elif ("a"<=a[i]<="z"):
#         new_str+=chr(ord(a[i])-32)
#     i+=1
# print(new_str)

# reverse a string without using slicing

# a = "HarshGupta"
# reverse = ""
# i=0
# while i<len(a):
#     reverse = a[i] + reverse
#     i+=1
# print(reverse)

# WAP to find palindrome

# a = "HarshGupta"
# reverse = ""
# i=0
# while i<len(a):
#     reverse = a[i] + reverse
#     i+=1
# print(reverse)

# if a == reverse:
#     print("the given string is palindrome")
# else:
#     print("its not a palindrome")

# WAP to check how many palindrome strings are there in a list

# list = ["harsh","mom","mam"]
# i=0
# while i<len(list):
#     if list[i]==list[i][::-1]:
#         print(f"{list[i]} is a palindrome")
#     i+=1

# WAP to exclude duplicate values present inside a list

# list = [10,10,30,40,30,80]
# l=[]
# i=0
# while i<len(list):
#     if list[i] not in l:
#         l.append(list[i])
#     i+=1
# print(l)

# WAP to replace space by * in a given string

# a = "Harsh Gupta"
# i=0
# l=''
# while i<len(a):
#     if a[i]==" ":
#         l=l+'*'
#     else:
#         l=l+a[i]
#     i+=1
# print(l)

# WAP to find sum of all the numbers which are divisible by either 3 or 7 between 1 to 50
# i=1
# sum = 0
# while i<51:
#     if i%3==0 or i%7==0:
#         sum = sum + i
#     i+=1
# print(sum)

# WAP to extract all the individual and collection values from a list seperately

# a = [1,2.2,True,50j,"str","1020",[4,5,6]]
# individual = []
# collection = []
# i=0
# while i<len(a):
#     if type(a[i]) in [int,float,complex,bool]:      # if type(a[i]) == int or type(a[i]) == float or type(a[i]) == complex or type(a[i]) == bool:
#         individual.append(a[i])
#     else:                                           # elif type(a[i]) == str or type(a[i]) == list:
#         collection.append(a[i])
#     i+=1
# print(individual)
# print(collection)

# WAP to fetch the list values inside a list only if it contains middle values

# a = [[1,2,3,4],[1,2,3],1,2,3,[1,4,5,6]]

# i=0
# while i<len(a):
#     if type(a[i])==list and len(a[i])%2!=0:
#         print(a[i])
#     i+=1


# WAP to fetch with only 2digit numbers from the given list

# a = [1,2,44,55,88,111,121,141]
# i=0
# while i<len(a):
#     if 10<=a[i]<=99:
#         print(a[i])
#     i+=1

# WAP to extract all the vowels and consonents respectively into 2 different string from the input string

# a = input("Enter your string : ")
# vowels = ""
# consonents = ""
# i=0
# while i<len(a):
#     if a[i] in "aeiouAEIOU":
#         vowels += a[i]
#     else:
#         consonents += a[i]
#     i+=1
# print(vowels)
# print(consonents)

# WAP to print all the factors of a given number

# a = int(input("enter a number : "))

# i=1
# while i<=a:
#     if a%i==0:
#         print(i)
#     i+=1

# WAP homogeneous int list and seperate even and odd numbers

# a = [1,2,3,4,5,6,7,8,9,10]
# i=1
# even = []
# odd = []
# while i<len(a):
#     if a[i]%2==0:
#         even.append(a[i])
#     else:
#         odd.append(a[i])
#     i+=1
# print(even)
# print(odd)

# WAP to find the individual datatype inside the list

# a = [1,2.2,True,50j,"str","1020",[4,5,6]]
# i=0
# individual = []
# while i < len(a):
#     if type(a[i]) in [int, float, complex, bool]:
#         individual.append(a[i])
#     i+=1
# print(individual)


# WAP to fetch all the individual data types values from the list collection except complex.

# a = [10,5j+15,'aditi','shrushti',11.8,[4,5,99],True,'True']
# fetch = []
# i=0
# while i<len(a):
#     if type(a[i]) in [int, float, bool]:
#         fetch.append(a[i])
#     i+=1
# print(fetch)

# WAP to fetch char inside a string only if it is at even index

# a = 'shrushti'
# i=0
# while i<len(a):
#     if i%2==0:
#         print(a[i])
#     i+=1

# WAP to reverse string and integer present in a list and check if its a palindrome or not

# a = ["harsh","MOM", "1221","Gupta"]
# i=0

# while i<len(a):
#     rev = a[i][::-1]
#     if a[i]==rev:
#         print(a[i])
#     i=i+1

# FIZZ-BUZZ program using while loop

# a = int(input("Enter a number : "))
# i=0
# while i<1:
#     if a%7==0 and a%5==0:
#         print("FIZZ - BUZZ")
#     elif a%5==0:
#         print("BUZZ")
#     elif a%7==0:
#         print("FIZZ")
#     i+=1

# if i/o = [1,4,9,16,20,25,41,48]
# then o/p = [1,4,4,1,0,0,1,3]

# a = [1,4,9,16,20,25,41,48]
# i=0
# output=[]
# while i<len(a):
#     b=a[i]%5
#     output.append(b)
#     i+=1
# print(output)

# WAP to reverse a string, without using slicing and if its a palindrome print the original string else concate with IPL

# a="MOM"
# i=0
# rev=""
# b = "IPL"

# while i<len(a):
#     rev = a[i]+rev
#     i+=1

# if a == rev:
#     print(a)
# else:
#     rev += b
# print(rev)

# WAP to fetch all the string values inside the list and reverse the string

# a = ["harsh", "gupta", 45,[1,2,3],"frd"]
# i=0
# rev_list = []
# while i<len(a):
#     if type(a[i]) == str:
#         b=a[i][::-1]
#         rev_list.append(b)
#     i+=1
# print(rev_list)

# ------------------------ convert smallcase alphabet to uppercase alphabet
# a="a"
# print(ord(a)-32)
# b= chr(ord(a)-32)
# print(b)

# addinton of @!#^

# a = ord("@")+ord("#")+ord("!")+ord("^")
# print(a)

# a = input("enter a string : ")
# i=0
# sum=0
# while i< len(a):
#     if a[i] in "`~!@#$₹%^&*()_|+=-[}{]\';'/.,<>?":
#         b=ord(a[i])
#         sum+=b
#     i+=1
# print(sum)

# WAP to fetch special char from the string, if the ascii value is even 

# a = input("Enter a special char : ")
# i=0
# while i<len(a):
#     if a[i] in "`~!@#$₹%^&*()_|+=-[}{]\';'/.,<>?":
#         if ord(a[i])%2==0:
#             print(a)
#     i+=1

# FOR LOOP ---------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Its a looping statement which will execute set of instructions repeatedly until the condition is satisified.
# Initialization and updation is not mandatory for looping in for loop.

# SYNTAX :-
# for var in collection:
#     S.B

# Collection :- str,list, tuple, set, dict, range
# 

# range: 
#       Its a inbuilt function which will give series of value based on the range passed.
# 
# SYNTAX:-
#       range(start,end+-1,updation)
# 
# example :
# print(list(range(1,10+1))) 

# Range function does not have capability to print on its own, so we need to typecasting for that.

# print(dict(range(1,10+1)))

# a = {'a':'one', b}

# ---------------------------------------------------------

# print(list(range(1,40+1,2)))
# print(list(range(0,40+1,2)))

# b=[]

# for i in range(1,35,3):
#     b.append(i)
# print(b)


# ----------------------------------------------------------------

# WAP to reverse a string

# s = 'harsh'
# rev = ''
# for i in s:
#     rev = i + rev
# print(rev)

# WAP to reverse a integer

# num = 4658
# rev = 0

# while num > 0:
#     digit = num%10
#     rev = rev*10+digit
#     num = num//10
# print(rev)


# WAP to find length of the dict without using len function

# a = {'a':'one', 'b':'two', 'c':'three'}
# count=0
# for i in a:
#     count += 1
# print(count)

# WAP to print key only if its individual data type and value only if its collection data type
# a = {'12':'he',5j:'hello', 8:[1,2,3], 'hi':45, 5.6:89, 12:(14,45,78)}

# for i in a:
#     if type(i) in (int,float,complex,bool):
#         if type(a[i]) in (list,tuple, str,set, dict):
#             print(i,':',a[i])
# d = {}
# for i in a:
#     if type(i) in (int,float,complex,bool):
#         if type(a[i]) in (list,tuple, str,set, dict):
#             d[i]=a[i]
# print(d)

# WAP to fetch value only if its integer datatype in collection

# a = [1,2,3,"hello",[4,5,6],5.8]
# b=[]
# for i in a:
#     if type(i) is int:
#         b.append(i)

# print(b)

# a={1:'one',2:45,67:3}
# for i in a:
#     if type(a[i])==int:
#         print(a[i])

# WAP to do add all the float number inside a dict collection only if key are of string data type
# key -> str
# value -> float

# a ={'he':10.2,'go':10, 'to':'bar', 'hello': 12.3, True:'false','good':50.6}
# s=0
# for i in a:
#     if type(i)==str and type(a[i])==float:
#         s+=a[i]
# print(s)


# WAP to fetch all the integer values from the list which are in even index.

# a= [10,20,4.5,20.3,True,45,89]

# for i in range(0, len(a)):
#     if type(a[i]) == int and i%2==0:
#         print(a[i])

# Whenever we want to find the value based on position, index or in any range use range function.

# find the sum of all the int value present inside a string.

# a = 'adi987shru123'
# sum=0
# for i in range(0, len(a)):
#     if "0"<=a[i]<="9" :
#         sum+= int(a[i])
# print(sum)

# only if in odd index
# a="a23vb6788jfd6778"
# sum=0
# for i in range(1, len(a),2):
#     if "0"<=a[i]<="9" :
#         sum+= int(a[i])
# print(sum)

# a="a23vb6788jfd6778"
# sum=0
# for i in range(0, len(a)):
#     if "0"<=a[i]<="9" and i%2==1 :
#         sum+= int(a[i])
# print(sum)

# --------------------------------------------------------------------------------------------------------------------------------

# SPLIT() :
#           Its a inbuilt function which is used to split the values  sequencially, and it works only on string datatype.
#           By default the values will be stored inside the list.
# SYNTAX : var.split() 

# a = "hi everyone good morning"
# print(a.split())
# print(a.split('o'))
# print(a.split('o',2)) # ,2 is for how many number of times particular character should be splited here "o" will be splited 2 times

# ---------------------------------------------------------------------------------------------------------------------------

# a = "hello madam how are you"
# print(a.split())
# print(a.split("a"))
# print(a.split("a",2))

# z = "sachin is god of cricket"
# print(z.split())
# print(z.split("i"))
# print(z.split("i",2))

# a="hell in a well"
# print(a.split())
# print(a.split("l"))
# print(a.split("l",3))

# WAP to get the following output:-
#                                   c= "hai students were are you"
#                                   o/p = ['hai':3, 'students':8, 'were':4,'are':3, 'you':3]

# c= "hai students were are you"

# sp= c.split()
# op={}
# for i in sp:
#     op[i]=len(i)
# print(op)

# WAP to fetch the int from the list only if its in odd index and the len is greater than 3.

# a=[1,2,4,8,5,68,15,18,80,87,41,98,49]

# for i in range(len(a)):
#     if i%2==1 and a[i]>3:
#         print(a[i])

# WAP to fetch all the special char from the string collection and if the length is greater than 5 print the result with "HII" else "BYE"

# a = 'sachin@#$%!^%dulkar'
# b=""
# for i in range(len(a)):
#     if a[i] in "`~!@#$%^&*":
#         b+=a[i]

                            # for i in b:
                            #     if len(b[i])>5:
                            #         b+="HII"
                            #     else:
                            #         b+="BYE"
# if len(b)>5:
#     b+="HII"
# else:
#     b+="BYE"
# print(b)

# WAP to fetch all the uppercase char present in odd index in a string.

# n= 'HhARarsssssSHhhh'
# for i in range(1,len(n),2):
#     if "A"<=n[i]<="Z":
#         print(n[i],end="")

# -------------------------------------------------------------------

# a="hello guys how are you"
# print(a.split())
# print("".join(a))

# WAP to find whether a number is prime or not
# a=int(input())

# for i in range(1,a+1):
#     if a==1:
#         print("Its neither prime nor composite")
#     if a%a==0 and a%1==0 and (a%):
#         print("Its a prime number")
#     else:
#         print("Its a composite number")

# for i in range(2,a):
#     if a%i==0:
#         print("not prime")
#         break
#     else:
#         print("Its a prime number")

# amstrong number

# num = int(input("Enter A Number : "))
# dum = num
# res=0
# l=str(num)

# while num!=0:
#     dl=num%10
#     res = res + dl **len(l)
#     num //= 10
# if res == dum:
#     print("Its amstrong number",res)
# else:
#     print("Its not a amstrong number")

# Disarium Number

# num = int(input("Enter a number : "))
# dum = num
# res = 0
# l=len(str(num))
# while num!=0:
#     dl=num%10
#     res = res + dl ** l
#     num //=10
#     l=l-1
# if res == dum:
#     print("Its a disarium number")
# else:
#     print("Its not a disarium number")

# Perfect Number

# num = int(input("Enter a Number : "))
# fact = 0
# i=1
# while i<num:
#     if num%i==0:
#         fact+=i
#     i+=1
# if fact == num:
#     print("Its a perfect number")
# else:
#     print("Its not a perfect number")


# --------------------------------------------------

# WAP to get the following o/p = 6

# a1 = '100110110'
# a2 = '111010110'

# count = 0

# for i in range(0,len(a1)):
#     if a1[i]==a2[i]:
#         count += 1
# print(count)

# --------------------------------------------------

# WAP to fetch middle value inside a list only if its a float value

# a=[1,3.3,4.2,6.2,5.6]

# for i in range(0,len(a)):
#     if len(a)%2 != 0:
#         if type(a[len(a)//2])==float:
#             print(a[len(a)//2])
#             break

# WAP to get the o/p = 'you are how hi'

# a ='Hi how are you'

# sp = a.split()
# # print(sp)
# rev = sp[::-1]
# # print(rev)
# jn = " ".join(rev)
# print(jn)

# break statement

# for i in range(0,21,2):
#     print(i)
#     if i==12:
#         break

# Nested for loop

# for i in range(1,8,3):
#     for j in range(1,5):
#         print(i,j)

# WAP to check user password until its true

# a = input("Enter password")
# i=0

# while i<len(a):

#     if a == "Harsh@123":
#         print(True)
#     else: 
#         print(False)

#     break

# WAP to check whether the list is homo or hetrogeneous

# a = eval(input("Enter a list : "))

# for i in a:

#     if type(a[0]) == type(a[1]):
#         print("It is homegeneous list")
#     else:
#         print("Its a hetrogeneous list")
#     break

# WAP to fetch complex values from the dict collection only if value is complex.
# a = {1:1j,2:5,3:4j}
# sum = 0
# for i in a:
#     if type(a[i])==complex:
#         # print(a[i])
#         sum+=a[i]
# print(sum)

# WAP to fetch all the odd values in the even index.

# a=[0,2,1,4,5,6,3]

# for i in a:
#     if i%2==0:
#         if a[i]%2 != 0:
#             print(a[i])

# WAP to fetch key pair only if its key is bool and value is str

# a = { True : "True", False : 5, True : [1,2], False:"False"}
# v={}
# for i in a:
#     if type(i)==bool and type(a[i])==str:
#         v[i]=a[i]
# print(v)

# -----------------------------------------------------------------------------------------------------------

# User Defined function:
#                       def f_name(args):
#                           statement block
#                           return value
#                       f_name(value)   # function call
# Numbers of args should be equal to number of values.
# def-> Its a keyword which is used to define a function
#  f_name -> Its a name given to the function
# Args -> These are the values passed into functions.

# -----------------------------------------------------------------------------------------------------------

# WAP to fetch only uppercase

# def upper():
#     a = "Hello"
#     b=""
#     for i in a:
#         if "A"<=i<="Z":
#             b+=i
#     print(b)
# upper()

# --------------------------------------------

# i/p :- 'Python class is easy'
# o/p :- {'Python':6, 'is':2}

# def test():
#     a = 'Python class is easy'
#     b = a.split()
#     c={}
#     print(b)
#     for i in range(0,len(b)):
#         if i%2==0:
#             c[b[i]]=len(b[i])
#     print(c)
# test()

# -----------------------------------------

# WAP to fetch only int values from the list only if its at even index and its divisible by 5

# def even():
#     a = [10,2,4,15,20,16.0,79,True]
#     for i in range(0, len(a),2):
#         if type(a[i])==int and a[i]%5==0:
#             print(a[i])
# even()

# -------------------------------------------

# WAP to toggle a string using 1st type of function

# def toggle():
#     a = "SrusHTi"
#     b=""
#     for i in a:
#         if "A"<=i<="Z":
#             b+=chr(ord(i)+32)
#         else:
#             b+=chr(ord(i)-32)
#     print(b)
# toggle()

# -------------------------------------------

# i/p :- 'How are you'
# o/p :- 'woh era uoy'

# def rev():
#     a = "How are you"
#     b=a.split()
#     re = ""
#     for i in range(0,len(b)):
#         if i==0:
#             re += b[i][::-1]
#         else:
#             re+=' '+ b[i][::-1]
#     print(re)
# rev()

# WAP to fetch special char from string

# def spc():
#     a = "harsh@123#$%"
#     b=""
#     for i in a:
#         if i in '`~!@#$%^&*)(_-+=|[}{]":>?<,./;':
#             print(i)
# spc()

# def spc():
#     a = "harsh@123#$%"
#     b=""
#     for i in a:
#         if i not in '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioplkjhgfdsazxcvbnm':
#             if ord(i)%2==0:
#                 print(i)
# spc()



# ----------------------------------------------------------------------------------------
# Function with arguments and no return value:
#                                   These are the function where only arguments are present but no return value
# SYNTAX:
#       def f-name(arg1, arg2,.....,arg(n)):
#           statement block
#       f-name(val1, val2, ......., val(n))
# The number of argument should be equal to number of values.

# ---------------------------------------------------------------------------------------

# def mul(a,b,c):
#     print(a*b*c)
# mul(1,2,3) 

# ----------------------------------
# find the vowels in the given string

# def vow(s):
#     a = s.split()
#     out = {}
#     for i in a:
#         b=''
#         for j in i:
#             if j in "AEIOUaeiou":
#                 b+=j
#             out[i]=b
#     print(out)
# vow('User Defined Function')

# -------------------------------------
# i/p = 'hii hello good morning'
# o/p = {'hii': 'i', 'hello': 'l', 'good':'gd','morning':'n'}

# def eo(s):
#     a = s.split()
#     out={}
#     for i in a:
#         if len(i)%2==0:
#             out[i]=i[0]+i[-1]
#         else:
#             out[i]= i[len(i)//2]
#     print(out)
# eo('hii hello good morning')


# ----------------------------------------

# def sj(s):
#     a = s.split()
#     out='*'.join(a)
#     print(out)
# sj('Hello Harsh')

# -----------------------------------------------------------------------------------------------
# functions with no arguments and with return value
# In this kind of function only return value will be present and no arguments are passed
# SYNTAX:
#       def f_name():
#           statement block
#           return value
#       print(f_name)
# -----------------------------------------------------------------------------------------------

# addn of 2 numbers

# def add():
#     a,b = 10,20
#     return a+b
# print(add())

# ----------------------------------
# WAP to extract all the string values from the list collection and try to join all the string using '#'

# def ex():
#     li = ["hello",1,"how",2.0,"are",3j,"you",True]
#     new = []
#     for i in li:
#         if type(i) == str:
#             new.append(i)
#             c = '#'.join(new)
#     return c
# print(ex())
# ----------------------------------
# ---------------------------------------------------------------------------------------------------------
# ZIP(): 
#       Its a inbuilt function used to provide more than one looping value in loops.
# SYNTAX:
#       for var1,var2,...,valn in zip(col1,col2,....,coln)
# number of iteration values, =number of collection
# ---------------------------------------------------------------------------------------------------------

# a = '101001001'
# b = '011011111'
# out = 0 
# for i,j in zip(a,b):
#     if i==j:
#         out+=1
# print(out)

# --------------------------------
# a = ['yahoo.com','google.in','hello.bye']
# # o/p : ['com','in','bye']
# out = []
# for i in a:
#     sh = i.split('.')
#     out.append(sh[-1])
# print(out)


# def splt():
#     a = ['yahoo.com','google.in','hello.bye']
#     out=[]
#     for i in a:
#         sh = i.split('.')
#         out.append(sh[-1])
#     return out

# print(splt())

# ----------------------------------------------------------------------------------------------------------------------------------------
# var.find('char') -> this find the first time occurence index of the char in the string

# var.rfind('char') -> this find the last time occurence index of the char in the string
# ----------------------------------------------------------------------------------------------------------------------------------------

# a = "harsh is harsh"
# b = a.rfind("harsh")
# c = "harsh is harsh".find("harsh")
# print(b)
# print(c)

# -------------------------------------------------------------------------------------------------------------------------------------------
# Functions with arguments and with return values.
# SYNTAX :
#           def f_name(arg1,...,argn):
#               Statement Block
#               return val1,...,valn
#           print(f_name(val1,...,valn))
# -------------------------------------------------------------------------------------------------------------------------------------------

# WAP to extract uppercase char from the string

# def upper(a):
#     b = ""
#     for i in a:
#         if 'A'<=i<='Z':
#             b+=i
#     return b

# print(upper('HaRsh'))


# def upper():
#     a = "HeLlo"
#     b=""
#     for i in a:
#         if "A"<=i<="Z":
#             b+=i
#     print(b)
# upper()

# def upper():
#     a = "HeLlo"
#     b=""
#     for i in a:
#         if "A"<=i<="Z":
#             b+=i
#     return b
# print(upper())


# def upper():
#     a = "HeLLO"
#     b = ""
#     for i in a:
#         if 'A'<=i<='Z':
#             b+=i
#     print(b)
# upper()

# --------------------------------------------------------------------------------------------------
# a = ['google.com','yahoo.in','python.py','gmail.com', 'linked.in']

# out = {}

# for i in range(0,len(a)):
#     b = a[i].split('.')
    
#     if b[1] not in out:
#         out[b[1]] = []
#     else:
#         out[b[1]]+=b[0]
#     # out[b[1]].append(b[0])
# print(out)

# ---------------------------------------------------------------------------------------------------------

#                               PATTERNS

# ---------------------------------------------------------------------------------------------------------

# print Diagonal

# *
#   *
#     *
#       *
#         *

# ----------------------------------------------------

# n = int(input("Enter the number : "))
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# --------------------------------------------------------

# print /

#         * 
#       *
#     *
#   *
# *
# --------------------------------------------------------

# n = int(input("Enter the number : "))
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if i+j==6:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# --------------------------------------------------------
# print X

# *       * 
#   *   *
#     *
#   *   *
# *       *
# --------------------------------------------------------

# n = int(input("Enter the number : "))
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if i+j==6 or i==j:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# ---------------------------------------------------
# *
# @ *
# @ @ *
# @ @ @ *
# @ @ @ @ *
# --------------------------------------------------------

# n = int(input("Enter the number : "))
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print("*", end=" ")
#         elif i > j:
#             print("@", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# --------------------------------------------------------
# * @ @ @ @ 
#   * @ @ @
#     * @ @
#       * @
#         *
# --------------------------------------------------------

# n = int(input("Enter the number : "))
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print("*", end=" ")
#         elif i > j:
#             print(" ", end=" ")
#         else:
#             print("@", end=" ")
#     print()

# -----------------------------------------------------------
#       * ! ! ! ! 
#       # * ! ! !
#       # # * ! !
#       # # # * !
#       # # # # *
# -----------------------------------------------------------

# n = int(input("Enter the number : "))
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print("*", end=" ")
#         elif i > j:
#             print("#", end=" ")
#         else:
#             print("!", end=" ")
#     print()

# -------------------------------------------------------
# 0 0 0 0 1 
# 0 0 0 1 0
# 0 0 1 0 0
# 0 1 0 0 0
# 1 0 0 0 0
# -------------------------------------------------------

# n = int(input("Enter the number : "))
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if i+j==6:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()

# ---------------------------------------------------
# * * * * * 
# *       *
# *       *
# *       *
# * * * * *
# ---------------------------------------------------

# n = int(input("Enter the number : "))
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if i==1 or i == n or j==1 or j==n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# ------------------------------------

# * * * * * 
# *   *   *
# * * * * *
# *   *   *
# * * * * *

# ------------------------------------

# n = int(input("Enter the number : "))
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if i==1 or i == n or j==1 or j==n or i==(n//2)+1 or j==(n//2)+1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# -----------------------------------------------------------------
#       *


# * * * * * * *
# -----------------------------------------------------------------

# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if i==n:
#             print("*", end=" ")
#         elif i == (n//2)+1 and j==(n//2)+1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# ----------------------------------------------------------------
#             *
#           *   *
#         *       *
#       *           *
#     *               *
#   *                   *
# * * * * * * * * * * * * *
# ----------------------------------------------------------------

# n = int(input("Enter a number: "))
# m=(n*2)-1
# for i in range(1, n+1):
#     for j in range(1,m+1):
#         if j-i == n-1 or i==n or i+j == n+1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# ------------------------------------------------
# 0 0 0 0 1 
# 0 0 0 1 2
# 0 0 1 2 2
# 0 1 2 2 2
# 1 2 2 2 2
# ------------------------------------------------

# n=int(input("Enter a num : "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j == n+1:
#             print("1", end=" ")
#         elif i+j>n+1:
#             print("2",end=" ")
#         elif i+j<n+1:
#             print("0",end=" ")
#     print()

# -----------------------------------------------------
        # 1,1     1,2     1,3     1,4     1,5
        # 2,1     2,2     2,3     2,4     2,5
        # 3,1     3,2     3,3     3,4     3,5
        # 4,1     4,2     4,3     4,4     4,5
        # 5,1     5,2     5,3     5,4     5,5

        #                 3,3     
        #         4,2     4,3     4,4     
        # 5,1     5,2     5,3     5,4     5,5

# --------------------------------------------------
# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# ------------------------------------------------------

# n=7
# for i in range(0,n+1):
#     for j in range(0,1):
#         print(i*"* ", end="")
#     print()

# ------------------------------------------------
# (1,1) (1,2) (1,3) (1,4) (1,5) 
# (2,1) (2,2) (2,3) (2,4) (2,5) 
# (3,1) (3,2) (3,3) (3,4) (3,5)
# (4,1) (4,2) (4,3) (4,4) (4,5)
# (5,1) (5,2) (5,3) (5,4) (5,5)
# ------------------------------------------------

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(f"({i},{j})", end=" ")
#     print()

# -------------------------------------------------
#     *
#    ***
#   *****
#  *******
# *********
# -------------------------------------------------
# n=7
# for i in range(1,n+1): # here n is the number of rows
#     space = n-i
#     stars = 2*i-1
#     print(space * " " + stars * "*")


# for i in range(1,n+1): # here n is the number of columns
#     if (i%2!=0):
#         a=int(n-i)
#         b= int(a/2)
#         print(b*"  ", end="")
#         for j in range(i):
#             print("*", end=" ")
#         print(" ") 


# ------------------------------------------------
'''
*********
 *******
  *****
   ***
    *
'''
# ------------------------------------------------

# n=5
# for i in range(n,0,-1): # here n is the number of rows
#     space = n-i
#     stars = 2*i-1
#     print(space * " " + stars * "*")


# ---------------------------------------------------------------------------------------------------------------------
# create 5 properties in class for an employee like, name, place, salary, grade, age.
# try to change the place using class and object, including, grade, age with object, name, salary using class
# ---------------------------------------------------------------------------------------------------------------------

# class Emp:
#     name= "Harsh"
#     place = "vasai"
#     salary = 30000
#     grade = 7.2
#     age = 22

# obj1 = Emp()
# Emp.name = "Harsh Gupta"
# print(Emp.name,Emp.place)
# obj1.name = "Harsh Harilal Gupta"
# print(obj1.name,obj1.place)
# obj1.grade = 8
# obj1.age = 23
# print(obj1.grade, obj1.age)

# Emp.name = "harsh gupta"
# Emp.salary = 35000
# print(Emp.name, Emp.salary)


# ---------------------------------------------------------------------------------------------------------------------
# customer:
#         name:
#         id:
#         place:
#         order:
#         price:
# obj1:
# obj2
# ---------------------------------------------------------------------------------------------------------------------

# class Customer:
#     c_name = "XYZ"
#     c_id =  1
#     c_place = "Mumbai"
#     c_order = "oldmonk"
#     c_price = 495

# print(Customer.c_name,Customer.c_id,Customer.c_order,Customer.c_place,Customer.c_price)
# obj1 = Customer()
# obj1.c_name = "ABC"
# obj1.c_place = "Navimumbai"
# obj1.c_id = 4
# obj1.c_order = "JagerMaster"
# obj1.c_price = "1200"
# print(obj1.c_name,obj1.c_id,obj1.c_order,obj1.c_place,obj1.c_price)
# print(obj1)
# obj2 = Customer() 
# obj2.c_name = "ABC"
# obj2.c_place = "Ghatkopar"
# obj2.c_id = 6
# obj2.c_order = "oaksmithsilver"
# obj2.c_price = 1000
# print(obj2.c_name,obj2.c_id,obj2.c_order,obj2.c_place,obj2.c_price)
# print(obj2)
# print(Customer())


# Here you will be having same memmory location for print(Customer()) and print(obj1)
# First Customer() creates an object → print it → destroy it → memory becomes free.
# Then obj1 = Customer() → new object created → Python sees free memory and reuses that spot.
# Thus memory address looks same.

# class Customer:
#     c_name = "XYZ"
#     c_id =  1
#     c_place = "Mumbai"
#     c_order = "oldmonk"
#     c_price = 495
# print(Customer())
# obj1 = Customer()
# print(obj1)
# obj2 = Customer() 
# print(obj2)

# ---------------------------------
'''
* 
 *
*
 *
*
'''
# ---------------------------------

# for i in range(1,6):
#     for j in range(1,3):
#         if i%2==1 and j==1:
#             print("*",end=" ")
#         elif i%2==0 and j%2==0:
#             print(" *", end=" ")
#     print()

# --------------------------
'''
* * * * * 
* * *   * 
* * * * *
*   * * *
* * * * *
'''
# --------------------------

# n=5

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n:
#             print("*", end=" ")
#         elif j==1 or j==n:
#             print("*", end=" ")
#         elif i==j or i==(n+1)//2 or j==(n+1)//2:
#             print("*",end=" ")
#         else:
#             print(" ", end=" ")
#     print()
    
# --------------------------------------
'''
* * * * * 
*       * 
*   *   *
*       *
* * * * *
'''     
# --------------------------------------

# n=5

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n:
#             print("*", end=" ")
#         elif j==1 or j==n:
#             print("*", end=" ")
#         elif i==j and i==(n+1)//2 and j==(n+1)//2:
#             print("*",end=" ")
#         else:
#             print(" ", end=" ")
#     print()
    

# ------------------------------------------------------------------------

'''                          CONSTRUCTOR-------------->>>>>>>>>

Constructor is a special / Dunder method in python.
Constructors can be called using __init__
Whenever an object is created constructor will get invoked automatically.
By default constructor will have one argument inside it(self).
constructor is used to declare and initialize the instance variables.
By default whenever we create a object default constructor will be present.

_ -> private
__ -> private pro[security purpose]
__ __ -> special method or Dunder method

'''
# ------------------------------------------------------------------------
# class Student:
#     def __init__(self,name,std):
#         self.name = name
#         self.std = std
    
#     def display(self):
#         print(self.name, self.std)

# obj1 = Student("vaibhav", 35)
# print(obj1.display())

# class Student:
#     def __init__(self,name,marks,rollno,age):
#         self.name = name
#         self.marks = marks
#         self.rollno = rollno
#         self.age = age
    
#     def display(self):
#         print(self.name, self.marks,self.rollno,self.age)

# obj1 = Student("vaibhav", 100, 9,14)
# print(obj1.display())
# obj2 = Student("Harsh", 100, 6,22)
# print(obj2.display())
# obj3 = Student("Raju", 80, 19,20)
# print(obj3.display())

# print(bin(10))

# print(10 and 60 or 0.0 or set() and 'mock' and 'Finish')

# print(10 or 90 and '' and 0.0 or 'Prati' and 90 or set())
# print(0 or 40 and 'hii' or set() and {} or 0.0 or False)
# print(45 or 'hitman' or 0.0 and set() and 0.5 or {} or 'Hey')

# ----------------------------------------------------------------------------------

'''difference between method and constructor

           Method                                     |                Constructor
                                                      |
______________________________________________________|___________________________________________________________________________
                                                      |
1. Methods can have any name                          |    1. Constructor name is always __init__
                                                      |
2. Per object we can have many methods.               |    2. Per object only one constructor can be created 
                                                      |
3. Inside method, we can write business, code logic   |    3. Inside constructor, only used to initialize th variable
                                                      |
4. Method is executed whenever we call the method     |    4. Constructor is executed whenever a object is created
   name.                                              |

'''
# ------------------------------------------------------------------------------------------------------------------------------

'''In modifying the properties we have:
                      i.) object method
                      ii.) class method

                                      ****************** OBJECT METHOD **********************

object method is used to access or modify the object members only.
SYNTAX : 
              def f_name(self):
                      statement block
              obj f_name(self, new)
              obj f_name(obj)

NOTE: When we want to access the object method using class we need to pass a object for it, but when we want to access the object method we no need to pass object for that, pass the value, which we wanted to be updated.'''

# ----------------------------------------------------------------------------------------------------------------------------------

# class std:
#     s_name = "Pratik"
#     s_age = 22
#     def __init__(self, grade, adress):
#         self.grade = grade
#         self.adress = adress
#     def display(self):
#         print(self.grade, self.adress)
#     def chg_grade(self, new):
#         self.grade = new
# obj1 = std("A2","Mumbai")
# obj1.display()
# obj1.chg_grade("A+")
# obj1.display()

# -----------------------------

# bank -> Task
# b_name and b_adress -> class property
# object property -> c_name, c_bal, c_adress, c_age and have atleast 2,3 objects to modify it

# class bank:
#      b_name = "sbi"
#      b_address = "vasai"
#      def __init__(self, c_name, c_bal, c_address, c_age):
#           self.c_name = c_name
#           self.c_bal = c_bal
#           self.c_address = c_address
#           self.c_age = c_age
#      def display(self):
#           print(self.c_name, self.c_bal, self.c_address, self.c_age)

#      def chg_c_name(self,new_name):
#           self.c_name = new_name
#      def chg_c_bal(self,new_bal):
#           self.c_bal = new_bal
#      def chg_c_address(self,new_address):
#           self.c_address = new_address
#      def chg_c_age(self,new_age):
#           self.c_age = new_age


# --------------------------------------------------------------------------------------------------------------
'''
                              *************__CLASS METHOD__***************
Class method is used to access or modify the class members only
SYNTAX : 
              def f_name(cls):
                      statement block
              obj1.f_name(args)
              class_name.f_name(args)
NOTE: Here in class method before defining it we should use a decorator called as @classmethod

Here we need to pass 'cls' as the argument inside the function
Its not mandatory to pass 'cls' as the variable  we can use anything, but according to standards we use 'cls' as arguments.
Here if we call the object method by using both object and class passing address of the object is mandatory.
'''
# --------------------------------------------------------------------------------------------------------------

# class std:
#      sname = 'Harsh'
#      saddress = 'vasai'
#      d=[]

#      def __init__(self, s_grade, t_name):
#           std.d+=[self]
#           self.s_grade = s_grade
#           self.t_name = t_name

#      def chg_grade(self, new):
#           self.s_grade = new

#      def chg_t_name(self, new):
#           self.t_name = new

#      def display(self):
#           print(self.s_grade, self.t_name)

#      @classmethod
#      def disp(cls):
#           print(cls.sname, cls.saddress)

#      @classmethod
#      def cls_sname(cls, new):
#           cls.sname = new

# obj1 = std('A', 'Harsh')
# obj1.display()
# std.cls_sname('Harsh Gupta')
# std.disp()
# std.display()   # Wrong way

# for i in std.d:
#      i.display()
# for i in std.d:
#      print(i.t_name)

# ----------------------------------------------------------------
# create 3 class members, 3 objects,with 3 object members change all the 3 class members

# class mem:
#     scl_name = 'MMEHS'
#     scl_address = 'Achole'
#     principle = 'Alan'

#     def __init__(self, std_clas, std_age, std_teacher):
#         self.std_clas = std_clas
#         self.std_age = std_age
#         self.std_teacher = std_teacher

#     def chg_all(self, new1, new2, new3):
#         self.std_clas = new1
#         self.std_age = new2
#         self.std_teacher = new3

#     def chg_std_clas(self, new):
#         self.std_clas = new

#     def chg_std_age(self, new):
#         self.std_age = new

#     def chg_std_teacher(self, new):
#         self.std_teacher = new

#     def display(self):
#         print(self.std_clas, self.std_age, self.std_teacher)

#     @classmethod
#     def cls_scl_name(cls,new):
#         cls.scl_name = new

#     @classmethod
#     def cls_scl_address(cls, new):
#         cls.scl_address = new

#     @classmethod
#     def cls_principle(cls, new):
#         cls.principle = new

#     @classmethod
#     def disp(cls):
#         print(cls.scl_name, cls.scl_address, cls.principle)

# obj1 = mem("7A", 14, "Pratik")
# obj1.display()

# obj2 = mem("9B", 15, "kartik")
# obj2.display()

# obj3 = mem("10A", 16, "menon")
# obj3.display()

# obj4 = mem.chg_all("11", 17, "chaubey")
# obj4.display()
# mem.disp()
# mem.cls_scl_name('SKC')
# mem.disp()

# mem.cls_scl_address('Vasai')
# mem.disp()

# mem.cls_principle('Stany')
# mem.disp()

# student1 = mem("8th", 14, "Mr. A")
# student1.display()

# ----------------------------------------------------------------------------------------
#                               LOCAL & GOBAL VARIABLE
# ----------------------------------------------------------------------------------------

# def abc():
#     a=10
#     print(a)
# def bca():
#     print(a)    # this will through an error

# abc()
# bca()

# -------------------------

# a=10
# def abc():
#     global a
#     a=777
#     print(a)
# def bca():
#     global a
#     a=111
#     print(a)
# abc()
# bca()

# ------------------------------------

# a=777
# def abc():
#     a=69
#     print(a)
#     print(globals()['a'])
# abc()

# a = 777

# def abc():
#     global a
#     print(a)
#     a = 69
#     print(a)

# abc()

# a, b = 20, 30
# c=a*b
# def mul():
#     a, b =4, 8
#     c = a*b
#     print(c*globals()['c'])
# mul()

# a, b = 20, 30
# c=a+b
# def add():
#     a, b =4, 8
#     c = a+b
#     print(c+globals()['c'])
# add()


# a, b = 20, 30
# c=a-b
# def sub():
#     a, b =4, 8
#     c = a-b
#     print(c-globals()['c'])
# sub()
    
# def wish(name='Harsh'):
#     print(name,"Good Morning")
# wish("Harsh Gupta")
# wish()


# def msg(name="harsh",msg = "hii",m="i am 22"):
#     print(name + " " + msg +" "+ m)
# msg()


# -------------------------------------------------------

# class bank:
#     bal = 2000
#     @classmethod
#     def deposit(cls,new):
#         cls.bal += new
#     @classmethod
#     def disp(cls):
#         print(cls.bal)
    
#     @classmethod
#     def withdraw(cls, new):
#         if cls.bal < new:
#             print("Insufficient Balance")
#         else:
#             cls.bal -= new

# bank.deposit(1000)
# bank.deposit(3000)
# bank.withdraw(4000)
# bank.disp()



# ------------------------------------------------------------------------------------------------------------------------------
'''
                                                    ABSTRACTION

      ABSTRACTION is a process for hiding the complexity of a system and display only essential feature for the end user.

                                                    ABSTRACTION METHOD

      These are the function/method which has function name but does not have function declarction or method body.
      SYNTAX:
              @abstract_method
              def add():
                      pass

                                                    ABSTRACT CLASS
A class which contains atleast one abstract method.

SYNTAX :
              class abc:
                      def add(a,b):
                              print(l+b)
                      def sub(a,b):
                              pass
'''
# -------------------------------------------------------------------------------------------------------------------------------

# from abc import ABC,abstractmethod

# class animal(ABC):
#     @abstractmethod
#     def makesound(self):
#         pass
# class dog(animal):
#     def makesound(self):
#         return 'bark'
# class cat(animal):
#     def makesound(self):
#         return 'meow'

# obj1 = dog()
# obj2 = cat()

# print(obj1.makesound())
# print(obj2.makesound())

# from abc import ABC, abstractmethod

# class cal(ABC):
#     @abstractmethod
#     def calculate(self):
#         pass

# class add(cal):
#     def calculate(self):
#         return "Addition"
# class sub(cal):
#     def calculate(self):
#         return "Subraction"

# obj1 = add()
# obj2 = sub()
# print(obj1.calculate())
# print(obj2.calculate())


# ------------------------------------------------------------------------------------------------------------------------------
'''Polymorphism
It is a process of a method, operator acting in different ways in different situation.
Ex:-'+'
10+10=20
'Hi'+'Bye'
Here addition operator is acting in 2 different way sin 2 different situation.
1)addition for real values(int, float)
2)Concatination for string values

*In polymorphism we have 2 types
1)method overloading
2)operator overloading

1)method overloading: It is using same method name for multiple types types
Ex:
"Java"
public class MethodOverloadingExample {
    public static void add(int a, int b) {
        System.out.println(a + b);
    }
    public static void add(int a, int b, int c) {
        System.out.println(a + b + c);
    }
    public static void main(String[] args) {
        add(10, 20);
        add(1, 2, 3);
    }
}

"Python"
def add(a,b):
    print(a+b)
prev=add
def add(a,b,c):
    print(a+b+c)
prev(10,20)
add(1,2,3)

In python method overloading is not possible so, we should use method overriding
->Monkey Patching: Since method overloading is not possible in Python, we use Monkey Patching where
  it stores method name inside a separate variable so that even though the methods names are same we
  can access both the method easily without any error. 
'''
# --------------------------------------------------------------------------------------------------------------------------------


'''
                                            ENCAPSULATION/ACCESS SPECIFIERS

1.] Protected access specifiers : 
                           Its a access specifiers which should provide protection for the members of the class, objects, but its not possible in python.

    [NOTE] : To make any variable or object as protected use single underscore(_) before it.

    SYNTAX : 
             class Hero : 
                _a = 10
                @classmethod
                def _disp():
                    statement block
                @staticmethod
                def _add(4d):
                    print c+d
                
                def __init__(self, var1, ..., varn):
                    self.var1 = var1
                    .
                    .
                    .
                    self.varn = varn
                obj1 = Hero(1.....100)
                obj1.disp()

2.] Private access specifiers : 
                               These are the access specifiers which will provide security to the members of the class & it will resist the access of memners of the class.

                               To declare the members of the class as private access specifiers the method or the variable must be start with double underscore (__).

    SYNTAX :
             class c_name:
                a = 10
                b=20
                c=30
                def __ch_b(self,new):
                    return __ch_b

                ob = c_name(40)
                print(__ch_b)
'''

class Morning:
    __m = 100

    def __init__(self, c, d):
        self.c = c
        self.__d = d

    def display(self):
        print(self.c + self.__d)

    @classmethod
    def ch.__m(cls, new):
        cls.ch__m = new

obj1 = Morning(10,20)
obj1.display()
print(obj1.__d)