#today i learnt about Multible Assignment , String Methods , type Casting

#multiple Assignment , they allow us to assign multiple variables in 1 line of code

name="Lisa"
Age="21"
Ugly= False

print(name)
print(Age)
print(Ugly)

#or it can be done like this:
TName, TAge  , TUgly ="Lisa" , 21 , False

print(TName,TAge ,TUgly)

#if assigning the same output we can simply
Lisa=Vee= Thando =Jane=30

print(Thando)


#STRING METHODS, they are basically used to manipulate strings

name="vhangani"

print(len(name)) #this returns the length of our string

print(name.find("g")) # this finds the index of the specified letter

print(name.capitalize()) #it capitalises the first letter of a string

print(name.upper()) #it changes everything to upper case

print(name.lower()) #changes everything to lower case

print(name.isdigit()) #checks if the string contains any digits

print(name.isalpha()) #checks if the string contains alphabets only

print(name.count("a")) #counts the number of specified letters

print(name.replace("a" ,"o")) #replaces the old character with a new one

#type casting - converting a datatype of a value to another datatype

a= 22 #int
b=25.3 #float
c="20" # string

a= str(a)
b= int(b)
c= float(c)

print(a)
print(b)
print(c)
