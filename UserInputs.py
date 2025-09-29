#This lesson was good to learn , from creating user inputs dialog , to adding them in the if statements and create a fully running program 
#user inputs are used to create  dialogue between a user and the terminal
#they always give you a string datatype
#so you need to convert to another data type if you want to use it

school= input("what is your school name :")

grade=int(input("what grade are you doing: "))

height=float(input("What is your height : "))

print("your school name is : "+ school)
print("And you and doing Grade: "+str(grade))
print("your height is :"+str(height))

import math

number= 25.73

print(round(number))# it rounds off your nuber to the nearest integer

print(math.ceil(number)) #it rounds the number up to the nearest integer

print(math.floor(number)) #it rounds the number down to the nearest integer

print((abs(number))) # it will tell you how far away a number is from 0

print(pow(number,3)) # it will raise the base to a power

a=2
b=4
c=6

print(min(a,b,c)) #it finds the minimum number from all the stated variables

print(max(a,b,c)) # it finds the maximum number from all the stated variables

#String Slicing
#-are used to create a substring by extracting from another string
#Indexing[] or slicing
#[start:stop:step]

name= "Vhangani Mugeri"

full_name=name[0:14:3] #the first index is inclusive while the lst index is exclusive
print(full_name)

#step is an optional field that we can set a value to
#basically how much we are increasing our index by between start and stop
reversed_name=name[::-1]
print(reversed_name)

#slice are basically used to create a slice object , which is re usable
#slice functions values are separated with a comma

websiteA= "http://NebaCollections.com"
websiteB= "http://google.com"

slice=slice(7,-4)

print(websiteA[slice])
print(websiteB[slice])

grade=int(input("Please Enter your Current grade : "))

if grade<=7:
    print('oh oh , You are still in Primary school')
elif grade>7 :
    print("Congragutions, You are in High school!")
    print("Enter a grade between 1 and 12 ! Thank you ")

    #logical Operators
    #-Used to check two or more conditional statement is true
temp= int(input("What is the temperature outside "))

if temp >=0 and temp<30: #in order for the entire line to run ,both statements must be true 
    print("the temperature is good today")
    print("You may go outside !!")
elif temp<0 or temp>30: # As long as one of these condition is true , the code will be executed 
    print("the temparature is not good today !")
    print("stay indoors")
