# wap to add two numbers
# def s():
#     a,b=10,20
#     print(a+b)
# s()

# wap program to fetch only upper case from the string call
# def ch():
#     a='Vedant'
#     b=''
#     for i in a:
#         if 'A'<= i <='Z':
#             b+=i
#     print(b)
# ch()

# wap for
# aa=''
# def d():
#     a='python class is easy'
#     di={}
#     sp=a.split()
#     for i in range(0,len(sp)):
#         if i%2==0:
#             di[sp[i]]=len(sp[i])
#     print(di)
# d()
        

# wap to fetch only integer values from the list only if it is in even index and it is divisible by 5
# def aa():
#     a=[10,2,4,25,18,16.0,79,True]
#     b=[]
#     for i in range(0,len(a)):
#         if type(a[i])== int :
#             if i%5==0 and i%2==0:
#                 b.append(a[i])
#     print(b)
# aa() 


# wap to toogle a string using first type of function

# def s():
#     a='SrUsHTi12'
#     b=''
#     for i in range(0,len(a)):
#         if 'a'<= a[i]<='z' :
#             b+=chr(ord(a[i])-32)
#         elif 'A'<= a[i]<= 'Z':
#             b+=chr(ord(a[i])+32)
#         elif '1'<= a[i]<='9':
#             b+=a[i]
#     print(b)
# s()


# def r():
#     a='how are you'
#     sp=a.split()
#     aa=''
#     for i in range(0,len(sp)):
#         if i ==0:
#             aa+=sp[i][::-1]
#         else:
#             aa+=' '+sp[i][::-1]
#     print(aa)

# r()


# wap to fetch special character from string collection
# def s():
#     a='veda^%$a'
#     aa=''
#     for i in range(0,len(a)):
#         if not ('a'<= a[i]<='z' or 'A'<= a[i]<='Z'or '1'<=a[i]<='9'):
#             aa+=a[i]
#     print(aa)
# s()

# def s():
#     a='veda^%$a'
#     aa=''
#     for i in range(0,len(a)):
#         if not ('a'<= a[i]<='z' or 'A'<= a[i]<='Z'or '1'<=a[i]<='9') and ord(a[i])%2==0:
#             aa+=a[i]
#     print(aa)
# s()

# ------------ FUNCTION WITH ARGUMENT AND NO RETURN VALUE---------------------------------
# def mul(a,b,c):
#     print(a*b*c)
# mul(3,3,3)

# def w(a):
#     b=a.split()
#     di={}
#     for i in b:
#         if i == 'aeiouAEIOU0':
#             di[b[i]]=i
#     print(di)
# w('user define function')
    

# def vol(a):
#     b=a.split()
#     di={}
#     for i in b:
#         c=''
#         for j in i:
#             if j in 'aeiouAEIOU':
#                 c+=j
#         di[i]=c
#     print(di)
# vol('user define function')

# def we(a):
#     b=a.split()
#     di={}
#     for i in b:
#         if len(i)%2==1:
#             di[i]=i[len(i)//2]
#         elif len(i)%2==0:
#             di[i]=i[0]+i[-1]
#     print(di)
# we('hi hello good morning')            

# a='aditi is missing'
# b=a.split()
# c='*'.join(b)
# print(c)

# ---------------------  FUNCTION WITH NO ARGUMENT AND  RETURN VALUE  --------------------------------------------

# def add():
#     a,b=10,20
#     return a+b
# print(add())

# 
# def st():
#     a=[1,2,'hi','yes',23,45.6,'a']
#     b=[]
#     for  i in a:
#         if type(i)== str:
#             b.append(i)
#             c='#'.join(b)
#     return c
# print(st())


# //////----------------zoop function---------------------

# a='101001001'
# b='101101111'
# count=0
# for i,j in zip(a,b):
#     if i == j:
#         count+=1
# print(count)