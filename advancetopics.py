'''                                                 lambda                                              '''

# a = int(input("enter 1"))
# b=int(input("enter 2"))
# var = lambda a,b:print("a is greater") if a>b else print("b is greater")
# var(10,20)

'''WAP to print if the number is even print square of the number if the number is odd print cube'''

# var = lambda a : print(f"{a} is even and its square is {a*a}") if(a!=0 and a%2==0) else print(f"{a} is odd and its cube is {a*a*a}")
# var(8)

'''WAP to check whether entered data is collection data type or not'''

# var = lambda a : print("single value data type") if(type(a) in [int, float, complex, bool]) else print("collection data type")
# var(21)

'''WAP to check whether the char is special char or not'''

# var = lambda a : print("Not a special char") if("A"<= a<="Z" and "a"<=a<="z" and "0"<=a<="9") else print("special char")
# var("@")


'''                                             MAP Function                                                '''

'''

Its used to perform same set of operation on each and every element of collection.

Map function will return address of the variable so it is mandatory to typecast to get the value.

SYNTAX :
        var = map(f_name, args)
        print(typecast(var))

'''

'''WAP to print square of all the numbers present in the list'''

# a = [1,2,3,4,5]
# var = lambda a : a**2
# var1 = map(var, a)
# # var1 = map(var, range(1,6))
# print(list(var1))

''' WAP to find length of each word present in string collection '''

# a = "Many are absent"
# b=a.split()
# print(b)

# var = map(lambda b:len(b),b)
# print(list(var))

# a = "good morning"
# b=a.split()
# var = map(lambda b: print(f"{b}:{len(b)}"),b)
# print(list(var))


a = 'a b c'
b = a.split()
var = lambda s : ord(s)
var1 = map(var,b)
print(list(var1))
# var = map(lambda b: print(f"{b}:{ord(b)}"),b)
# print(list(var))

''' FILTER Function'''

'''In case of map function the number of input is equal to number of output.
To over come the above scenario we use filter function.
In filter function we can filter the values which are neccessary or required 

SYNTAX:
        var = Filter(f-name, collection)
        print(var)

'''
