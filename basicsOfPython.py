
#......................................print in console/terminal..............................

#print("Hello World") 

#......................................variable declaration...................................

# name = 'Deepak'
# age=25
# isAdult=True
# bTechMarks=68.90
#print("My Details",name,age,isAdult,bTechMarks)

#.......................................Recieving Input........................................

# something = input("Enter Something: ") # will take input from user and return a string
# print(something)

#.......................................Type conversion.........................................

# type of data in python Number, String, Boolena
#int(value)
#float(value)
#bool(value)
#str(value)

#Exa 1
# birhtOfYear = int(input("Enter Year of Birth: "))
# print("You are "+str(2024-birhtOfYear)+" year old.") 
#python only concate only string does not concat string with number or other data type

#Exa 2
# num1 = float(input("Enter 1st N0: "))
# num2 = float(input("Enter 2nd N0: "))
# print("is 1st number greater: "+str(num1>num2))
# print("Sum of 1st and 2nd No: "+str(num1+num2))

#..........................................Strings.............................

# course = "Basics of Python";
# print(course.upper()) #return upper case
# print(course.lower()) #return lower case
# print(course.find('a')) #retur first matched index
# print(course.find('of')) #return first matched index
# print("Python" in course)#will return boolean
# print(course.replace('Python','Javascript')) #will replace Python with Javascript and return a new string

#....................................Arithmatic Operators.......................

# +, -, /, //, %, *, **
#/ -> return floating number
# Exa : 10/3 -> 3.33333
# // -> return a whole number or quotient
#Exa : 10//3 -> 3
# ** -> return a calculated power
#Exa : 10**4 -> 10*10*10*10 -> 10 to the power of 4 is 10000

#......................................operator precedance.......................

# result = (((10+3)*2)/2)+4-2
#print(result) #15

#......................................comparison................................

# ==, >= ,<= ,< ,> ,!=

#......................................Logical Operators............................

# and, or, not
# num = 10
# print(num>5 and num<20) #True
# print(num>15 or num<20) #Frue
# print(not num<20) #False

#......................................control statement..............................

# temp = 35
#if
# if temp>30:
#     print('Too Hot')
#     print('Drink Water')

#elif if ladder
# temp = 10
# if temp>30:
#     print('Too Hot')
#     print('Drink Water')
# else :
#      print("it is a moderate or cold")

# temp=25
#elif if ladder
# if temp>30:
#     print('Too Hot')
#     print('Drink Water')
# elif temp>20 and temp<30:
#     print("it is a nice day")
# else :
#      print("it is a too cold")

#......................................while loop...................................

# i=1
# while i<=5:
#     print(i)
#     i=i+1

# i=1
# while i<10:
#     print(i*'*')
#     i=i+1
    
#....................................Lists -> as like array.............................

# names = ['Deepak','Shyam','Krishna','Ram','Akki','John','Balram']
# for name in names:
#     if name =="John":
#         break;#stop iteration
#     if name =="Ram":
#         continue; #skip the current iteration
#     print(name)
# names[0]='Deepak Gupta'
# print(names[0]) #return 0th element
# print(names[1]) #return 1th element
# print(names[-1]) #return last index element
# print(names[-2]) #return 2nd last index element
# print(names[0:3]) #return elenet from 0th to (3-1)th index

#List Methods
# numbers = [1,2,3,4,5,6,7]
# numbers.append(10)#will push 10 in the last
# numbers.insert(0,11) #first parameter index and 2nd is value
# numbers.remove(11) #will remove 11 from list
# numbers.clear()#will make the list empty
# print(numbers)
# print(2 in numbers) #will return boolean true/false
# print(len(numbers)) #will return length of the list

#................................for loop....................................

# num = [1,2,3,4,5,6,7]
# for item in num :
#     print(item)

#.................................range function...............................

# n = range(5) # generate a sequence of number from 0 to 4
# for item in n :
#     print(item)

# n = range(50,55) # generate a sequence of number from 50 to 54
# for item in n :
#     print(item)

# n = range(5,15,2) # generate a sequence of number from 5 to 13 with step by 2 -> 5,7,9,11,13
# for item in n :
#     print(item)

#..............................Tuples similar as a array...........................

#tupels are immutable cant change after declaration
#number = (1,3,2,3,4,5,3);
#number[0]=10 #will throw an error
# print(number.count(3)) #will the print the occurance of 3 in a tuple
# print(number.index(3)) #will print first matched index of 3

#.............................set.......................................................

#items = {10,10,11,34,15,15};
#print(items)#{10, 11, 34, 15}

#..............................disctionary like a object in js................................

# marks = {"eng":90,"math":66,"hindi":88}
# print(marks['eng'])
# marks["phy"]=77
# marks["math"]=100

#.............................Functions..................................................

#in-built function
#int(), bool(),float()
#Module Functions -> a file which has related variables and function
#exa
# import math
# print(dir(math))

# from math import sqrt #will import sqrt function from math module
# print(sqrt(16));
# from math import * #will import all function from math module
# print(sqrt(25));
 
#user defined function

# def function_name(parameter):
#     print(parameter)

# function_name(arguments)

# def print_sum(num1,num2):
#     print(num1+num2);

# print_sum(10,20)

# def print_sum_defaultParameter(num1,num2=100): #num2 is default parameter
#     print(num1+num2);

# print_sum_defaultParameter(10)

