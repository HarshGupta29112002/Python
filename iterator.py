'''
Iterator :
        Iterator means traversing through a collection sequentially one after the another value to do this process we call it as iterator. 
        "for loop" is a inbuilt iterator. To user iterator manually we have 2 functions:
        1.] iter function
        2.] next()

        iter function:
                It is a function which is used to store the initial address of ot collection.

                SYNTAX:
                    iter_var = funct_name(collection)
        next():
                It is used to iterate to the value one by one sequentially.

            a = [1,2,3,4,5]


'''
# a = [1,2,3,4,5]
# for i in a:
#     print(i)

# i = iter(a)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# ------------------------------------------
'''

Generator :
            Generator is used to generate a sequence of value sequentially.
            we can create a sequnce of value using 'yield' keyword.

            SYNTAX : 
                    def abc():
                        print("hi")
                        print("neha")
                        print(list(abc()))

'''

def abc():
    print("Morning")
    yield 1
    print("evening")
    yield 2
    print("night")
    yield 3

print(list(abc()))

'''
NOTE :  To call a user defined function as generator  we should contain one yield keyword.
    Difference between yeild and return keyword :-

    RETURN                                                        |          YIELD
__________________________________________________________________|__________________________________________________________________
It will not work more than 1 time for some function               | we can use yield for multiple time for a single function
                                                                  |
No typecasting is required to print the values                    | Type casting is required is yield.
                                                                  |

'''
# decorator 
# file handling
# db connecti
# package architecture
# regular expression
# multithreading




# WPA to find highest of 2 numbers in lambda function

# wpa to filter even only from the list using filter and lambda function





