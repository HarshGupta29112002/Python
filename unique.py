# if (0.1+0.2 == 0.3):
#     print ('True')
# else:
#     print ('False')

'''
The answer is false due to floating-point precision errors in binary representation.

Q.} Why it happens:

->  Computers represent floating-point numbers (like 0.1, 0.2, and 0.3) in binary using a format called IEEE 754.
    Numbers like 0.1 and 0.2 cannot be exactly represented in binary.
    So, 0.1 + 0.2 results in a number very close to 0.3, but not exactly 0.3.

Q.} How to fix it:

->  Use the `math.isclose()` function to compare floating-point numbers with a tolerance.
    Example:
        import math
        if math.isclose(0.1 + 0.2, 0.3):
            print('True')
        else:
            print('False')
'''

# import math
# if math.isclose(0.1 + 0.2, 0.3):
#     print('True')
# else:
#     print('False')


# ----------------------------------------------------------

# adding without + operator

# a=10
# b=20
# count=a
# while(b>0):
#     count+=1
#     b-=1
# print(a,b)






# -----------------------------------------------------------------------

# emi = 2000
# yr_emi = emi * 12 #24000
# rate = 0.1
# comp_yearly = 0
# fv = yr_emi
# interest = 0
# for i in range(1,11):
#     interest = yr_emi * rate
#     comp_yearly = fv + interest
# print(f"interest = {interest}")
# print(f"final value = {comp_yearly}")


# for i in range(1,11):
#     interest = (comp_yearly + yr_emi)*rate
#     comp_yearly += yr_emi 

# print(comp_yearly)



# fv = 413104.04078866297
# p = 2000
# r = 1
# n = 10*12

# fv = p * ((((1+r)**n)-1)/r) * (1+r)
# print(fv)




                                    # "min-max char:password"
# **************************************************************************************************************************
                                    # "1-3 a: abcdef"
                                    # "2-4 b: cdefghi"
                                    # "5-7 c: ccccccc"
# **************************************************************************************************************************

# def bool(rule_and_password):
#     # Split the rule and password
#     rule_part, password = rule_and_password.split(": ")
    
#     # Further split the rule part to get min, max, and the character
#     range_part, char = rule_part.split(" ")
#     min_count, max_count = map(int, range_part.split("-"))
    
#     # Count the occurrences of the character in the password
#     char_count = password.count(char)
    
#     # Check if the frequency is within the allowed range
#     if min_count <= char_count <= max_count:
#         print("Valid Password")
#     else:
#         print("Invalid Password")

# # Example usage
# rule_and_password = input(str())
# bool(rule_and_password)




a = ["hello", "hi", "harsh",10,20,30]

def abc():
    for i in a :
        if type(i)==int:
            yield i
print(list(abc()))