#so in this lesson i learned about loops in python including While loop , For loops , lists, 2D lists , and loop control statement , the (break, continue and pass)
#it was quiet challenging but also fun to do

#   While Loops - A statement that will execute its block of code as long as its condition remains true
#it is unlimited /infinite , depending on the condition

while 1== 1:
    print()
#in the following program we will prompt the user to enter their name , if they skip , the code will
#continue to run until they do so

name= ""
while len(name)==0:
    name=input("please Enter Your Name")

print("Hello" +name)

#For loop - A statement that will execute its block of code for a limited amount of time

#let's create a for loop that will count from 1 to 20

for i in range(20):
    print(i)

#this is a range between 2 numbers

for b in range(20,51):
    print(b)

for count in range(5,0,-1):
#this is to show that it is going to begin counting from 1 and end at 0, reducing 1 at a time


    print(count)
    time.sleep(1) # we are going to use 2 seconds at a time !
    count+1
print("Happy Graduation day")

#Nested Loops ->is a general concept of having one loop inside of another.whether it is a while or a for
#so the inner loop will finish all its iterations before finishing the one iteration of the outer loop

#in this program we will draw a square

rows=int(input("Enter the number of rows: "))
column=int(input("Ether the number of columns: "))
symbol=input("Enter the symbol you want to use")

for r in range(rows):
 for c in range(column):
        print(symbol, end="")

    

#Loop control statements -we are basically changing the loops executions from their normal sequence

#break - used to terminate the loop entirely
#continue-skips to the next iteration of the loop
#pass-does nothing , acts as a placeholder

#this program will continue to run until I enter my name

while True:
    name=input("Enter your name : ")
    if name!="":
        break #remember a break is used to terminate th ehwole blocl of code enterely

    
    #in this code we are going to  display the numbers without the dashes(-)

call="072-642-9983"

for i in call:
    if i =="-":
        continue #this one skips to the next iteration of the loop

    print(i ,end="")

#Lists-are used to store multiple elements in a single variable

car=["Golf8 GTI","VW TIAGO","Rline","Porche","Benz GLE"]
car.append("mazda")# add last element in the list
car.pop() #removes the last element
car.remove("Porche") #removes an element
car.insert(3,"BMW M4") #replaces an element
car.sort()#it lists the cars alphabetically
car.clear()# clears the list
print(car[1]) #we are choosing to print the second car in the list

#for i in car:
    #print(i)   # we are printing all the list of cars

#2D list -multi Dimensional list(list inside of another list)

drinks=["cocacola","sprite","fanta Pine"]
clothes_brand=["Nike","Adidas","Puma"]
Cars=["VW Polo","POLO GTI","VW TIAGO","BMW"]

All=[drinks, clothes_brand,Cars]


print(All[0][1])# it will access the first variable and the second element
print(All[1][0]) # it will access the second variable and the first element 
print(All[2][2])# it will access the third variable and the third element in the list
print(All[1][2]) # it will access the second variable and the third element in the list 


