'''                                                 lambda                                            

SYNTAX:
        lambda arguments: expression

                lambda -> keyword used to declare an anonymous function.

                arguments -> one or more arguments (just like a regular function).

                expression -> a single expression that is evaluated and returned.


'''

# addition of 2 numbers

# add = lambda a,b: print(a + b)
# add(2,3)

# Square of 2 numbers

# sq = lambda num,power : num**power
# print(sq(2,3))

# sq = lambda a: a**2
# print(sq(2))


# a = int(input("enter 1"))
# b=int(input("enter 2"))
# var = lambda a,b:print("a is greater") if a>b else print("b is greater")
# var(10,20)

# var = lambda a, b : print("a>b") if a>b else print("a<b")
# var(5,6)


'''WAP to print if the number is even print square of the number if the number is odd print cube'''

# var = lambda a : print(f"{a} is even and its square is {a*a}") if(a!=0 and a%2==0) else print(f"{a} is odd and its cube is {a*a*a}")
# var(8)

# var = lambda a : print(a**2) if a%2==0 else print(a**3)
# var(2)
# var(3)

'''WAP to check whether entered data is collection data type or not'''

# var = lambda a : print("single value data type") if(type(a) in [int, float, complex, bool]) else print("collection data type")
# var(21)

# var = lambda a : print("Its a collection datatype") if type(a) not in [int, float, complex, bool] else print("Its not a collection datatype")
# var(5)

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


# num=[2,4,6,8]
# lam = lambda i:i**2
# m=map(lam, num)
# print(set(m))


''' WAP to find length of each word present in string collection '''

# a = "Hello how are you"
# sp = a.split()

# lam = lambda i: f"{i} : {len(i)}"

# var = map(lam, sp)
# print(list(var))

# a = "Many are absent"
# b=a.split()
# print(b)

# var = map(lambda b:len(b),b)
# print(list(var))

# a = "good morning"
# b=a.split()
# var = map((lambda i: f"{i} : {len(i)}"),b)
# print(list(var))




# sam = lambda w:(w,len(w))

# print(dict(map(sam,input().split())))

# print(dict (map ( lambda w:(w,len(w)), input().split() ) ) )



# a = 'a b c'
# b = a.split()
# var = lambda s : ord(s)
# var1 = map(var,b)
# print(list(var1))
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


# nums = [1, 2, 3, 4, 5]
# lam = lambda i : i%2==0
# mp = map(lam,nums)
# print(list(mp))



# evens = map(lambda x: x % 2 == 0, nums)
# print(list(evens))  # Output: [2, 4]

# evens = filter(lambda x: x % 2 == 0, nums)
# obj = list(evens)
# print(type(evens))  # Output: [2, 4]

# print(obj)






class MyClass:
    def __init__(self):
        self.__secret_data = "Hidden"

    def __private_method(self):
        print("This is a private method")

    def public_method(self):
        print("Accessing private method from public method:",end=" ")
        self.__private_method()


obj = MyClass()

obj.public_method()
# ✅ Output: Accessing private method from public method:
#           This is a private method

obj.__private_method()
# ❌ Error: AttributeError: 'MyClass' object has no attribute '__private_method'
