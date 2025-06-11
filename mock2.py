# '''

# 1.] Hybrid inheritance? Explain a calculator example with hybrid inheritance
# --> 
# Hybrid inheritance combines multiple inheritance types into one class hierarchy, allowing for complex and flexible relationships. In a calculator example, you could combine single, multiple, and hierarchical inheritance to model a calculator that performs basic operations, has advanced functions, and can be categorized as different types. 


# '''

# class Normal:
#     def add(self, a, b):
#         return a + b
    
#     def subtract(self, a, b):
#         return a - b

# class Sifi:
#     def power(self, a, b):
#         return a ** b
    
#     def square_root(self, a):
#         return a ** 0.5

# class CombinedCalc(Normal, Sifi):
#     def multiply(self, a, b):
#         return a * b

# class AdvancedCalc(CombinedCalc):
#     def divide(self, a, b):
#         if b != 0:
#             return a / b
#         else:
#             return "Cannot divide by zero"
        
# calc = AdvancedCalc()

# print("Add:", calc.add(10, 5))
# print("Subtract:", calc.subtract(10, 5))
# print("Multiply:", calc.multiply(10, 5))
# print("Divide:", calc.divide(10, 2))
# print("Power:", calc.power(2, 3))
# print("Square Root:", calc.square_root(16))


# '''

# 2.] Explain single, multi & multiple inheritance with example
# -->

# '''
# # SINGLE LEVEL INHERITANCE
# # In single level inheritance one child class inherits from one parent class.

# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# d = Dog()
# d.speak()  
# d.bark()   

# # MULTI-LEVEL INHERITANCE
# # A class inherits from a class which itself inherits from another class.

# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal): 
#     def bark(self):
#         print("Dog barks")

# class Puppy(Dog):  
#     def weep(self):
#         print("Puppy weeps")

# p = Puppy()
# p.speak() 
# p.bark()  
# p.weep()

# # MULTIPLE LEVEL INHERITANCE
# # A class inherits from more than one parent class.

# class Father:
#     def skills(self):
#         print("Father: Gardening, Cooking")

# class Mother:
#     def skills(self):
#         print("Mother: Art, Singing")

# class Child(Father, Mother): 
#     def skills(self):
#         print("Child: ", end="")
#         super().skills()  

# c = Child()
# c.skills() 


# '''

# 3.] Explain class & object method with example
# -->

# '''
# # __________CLASS__________
# # A class is like a blueprint for creating objects.
# # It defines the structure and behavior that the objects created from the class will have.

# class ClassName:

#     def __init__(self, arg1, arg2):
#         self.arg1 = arg1
#         self.arg2 = arg2

#     def method_name(self):
#         print("Doing something")


# # __________OBJECTS__________
# # An object method works on individual object data. It takes self as the first parameter.

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def show_info(self):
#         print(f"Name: {self.name}, Grade: {self.grade}")

# s1 = Student("Harsh", "A")
# s1.show_info()

# # Explain Constructor with example

# # A constructor is a special method in a class that is automatically called when you create a new object from that class. In Python, the constructor method is named __init__.

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def show_info(self):
#         print(f"Name: {self.name}, Grade: {self.grade}")

# s1 = Student("Harsh", "A")
# s1.show_info()
        

# # Explain Polymorphism with examples

# # Polymorphism means "many forms". In OOP, it allows objects of different classes to be treated as objects of a common superclass.
# # The same method name can have different implementations in different classes.

# class Cat:
#     def sound(self):
#         print("Meow")

# class Dog:
#     def sound(self):
#         print("Bark")

# def animal_sound(animal):
#     animal.sound()

# d = Dog()
# c = Cat()

# animal_sound(d) 
# animal_sound(c)  


# Functions with arguments and no return value

# def add(a,b):
#     print(a+b)
# add(4,5)

# FUNCTION WITH NO ARGUMENT AND  RETURN VALUE

# def add():
#     a,b=10,20
#     return a+b
# print(add())

# functions with arguments and with return values

# def ad(a):
#     b=''
#     for i in a :
#         if 'A'<= i <='Z':
#             b=b+i
#     return(b)
# print(ad('HarSh'))

# functions with no arg and no return value

# def aa():
#     a='HarSh'
#     b=''
#     for i in a :
#         if 'A'<= i <='Z':
#             b=b+i
#         print(b)
# aa()