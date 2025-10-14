#this was a very challenging and most confusing lessions i learnt , but i managed to complete the programs 
#Functions , Retun Statement , keyword arguments, string formart

#Functions- Block of code that is only executed when it is called

def details(name, last_name,age):
    print("Hello Mr "+name+" " +last_name
          +" you are "+str(age)+" years old")
    print("Have a lovely day ")



details("vhangani","mugeri",22)

#RETURN STATEMENTS- functions send python values/objects back to the caller , these values
                    #are known as the function return values

# in this program , we are going to multiply 2 numbers and return the results using functions

def numbers(num1,num2):
    results= num1*num2
    return results

x=numbers(10,5)

print(x)

#Keyword Argument
#- arguements proceded by an identifier when we pass them to a function
#-the order of the arguements doesn't matter , unlike positional arguement that we used previously
#-python knows the name of the arguements that our function receives

def names(first_name, middle, last):
    print("hello "+first_name+" "+ middle+" "+ last)

names(last="mugeri",middle="vee",first_name="Vhangani")

#Nested Function-#Function calls inside other function calls
            #-Innermost functions are resolved first
            #-return value is used as an argument for the next outer function
#asking a user to enter a positive number is they choose not to , we manipulate it
print(round(abs(float(input("Enter a whole positive number: ")))))

#Variable Scope- the region that a variable is recognized
               #- A variable is only available only inside a region that is created
               #-A global and locally scope version of a scope can be created

name="Vee" #global scope (Available inside and outside of a function

def display_name():
    name="Mugeri" # Local scope (available only inside this function)
    print(name)

display_name()
print(name)

# *args- parameters that pack all arguments into a tuple
       #-useful so that a function can accept a varying amount pf arguments

def add(*stuff):
    sum=0
    stuff=list(stuff)
    stuff[0]=0
    for i in stuff:
        sum += i
        return sum

print(add(1,2,3,4))

#*Kwargs- parameters will pack all aeguments into a dictionary
        #-useful so that a function can accept a varying amount of keyword arguments

def names(**kwargs):
    #print("hello"+kwargs['first'] + " " +kwargs['last'])
    print("hello", end= " ")
    for key,value in kwargs.items():
        print(value, end=" ")

names(tittle="hello Mr", first='Vhangani',middle="Vee",last="Mugeri")








