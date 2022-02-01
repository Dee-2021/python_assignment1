#task1 :Create three variables in a single line and assign values to them in such a manner that each one of
#them belongs to a different data type.
x = 2.01
z = 'Deepika'
y = 1

print(type(x))
print(type(y))
print(type(z))


#Task2 :Create a variable of type complex and swap it with another variable of type integer.

x = 5 + 6j
y = 6
z = x+y
print(type(x))
print(type(y))
print(z)

print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

 
# code to swap 'x' and 'y'
x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)


#task3 :Swap two numbers using a third variable and do the same task without using any third variable.

x = 10
y = 5
 
# code to swap
# 'x' and 'y'
 
# x now becomes 50
x = x * y
 
# y becomes 10
y = x // y;
 
# x becomes 5
x = x // y;
 
print("After Swapping: x =",
              x, " y =", y);
 
 # do the same task without using any third variable.

x = 20
y = 30
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
# code to swap 'x' and 'y'
x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)

#task4 : Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
#Version.

print ("Hello world") 

a = 7/2
print(a)

a = 7/2 #In python2.x answer for a = 3 .
# Python 2 and 3:
print('Hello', 'Guido')


#task5:Write a program to complete the task given below:
#Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
#another variable called z. Add 30 to z and store the output in variable result and print result as the
#final output.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
sum = a+b
print(sum)
c = sum
res = c+30
print(res)



#task6 :taking input and print datatype
age = 23
print("Dtatype : ", type(age))
str = 'python'
print("Datatype :",type(str))
float = 3.14
print("Datatype :",type(float))
complex = 3 + 5j
print("Datatype :",type(complex))


#task7 :Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
#UPPERCASE.
#initialize string using method title and replace

test_str = 'myname_is_deepika' #snak case
print("the original string is : " + test_str)
res = test_str.replace("_"," ").title().replace(" ", "")
print("the string after changing case : " + res) #pascal case


#task8 : If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
#again. Will it change the value? If Yes then Why?


#Yes, variables in Python can be reassigned to a new value that is a different data type from its current value. In fact, variables can be reassigned to any valid value in Python, regardless of its current value.
# This variable is initially assigned as a string. 

var = "Hi Deepika"

# It can be reassigned to any other value, regardless of the type.
var = 30
var = False
#This is possible due to the fact that the data types are dynamically typed in python.







