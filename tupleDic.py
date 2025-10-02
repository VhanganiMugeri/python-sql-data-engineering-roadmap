#I just completed the basics of tuple, sets , dictionaries , they work almost the same way but they have differences
# i also did the index operator which was pretty simple because i have worked with it before 

#tuple - collection of unordered and unchangable data , used to group related data together

#they are more like lists , they use a set-up para synthesis

student=("Vhangani","22","Male")

print(student.count("22"))  #this one counts , how many times does "22" appear in the list
print(student.index("Vhangani"))   #it tells the index at which the specified variable is at

#if i want to call everything that is within the student variable I :

for x in student :
    print(x)

    #to check if a certain variable exist we :
if "bongani" in student:
    print("yes he exist")

#sets -collection which is unordered , and has no  duplicate values

laptops={"acer","dell","lenovo","big"}
cars={"benz","mahindra","nissan"}

#these are some of the functions of sets

laptops.add("hp") # we are adding an element to the laptops variable
cars.remove("benz") # we are removing the called element
cars.clear()

cars.update(laptops) # this will add all the cars elements to cars


# we can all see the differences and the similarities of both variables

for x in laptops:
    print(x) #it will display all the elements that are stored in laptop variable

#dictionaries - they are changeable , unordered collection of unique key , value pairs.
# they are fast because they use hashing , they allow us to access a value quickly

# this is a program that will store countries(key) and their provinces(value)

provincies={'Eastern Cape':'Bhisho','Gauteng':'Johannesburg','limpopo':'polokwane','Freestate':'Bloem'}

#now lets access the values using associated key

print(provincies['Gauteng'])
print(provincies['limpopo'])

#lets try to call a key that does not exist using the get method to avoid errors

provincies.update({'kwazulu-natal':'pietermarizburg'})
print(provincies.get('kwazulu-natal'))

provincies.update({'Gauteng':'jozi'})
print(provincies.get('Gauteng'))


#functions of dictionaries

print(provincies.keys())# which will display the keys only
print(provincies.values()) #which will display the values only

for key,value in provincies:
    print(key,value) # it will display everything


#index operator- basically give you access to a sequence's element

name='vhangani MUGERI'

#lets change the first letter to upper case using if and index

if name[0].islower():
    name=name.capitalize()

#lets manipulate it using substring

    first_name=name[0:8].upper()  #it changes from start(0) to finish(8) of the letter and changes everything to uppercase
    last_name=name[9:].lower()
    last_character=name[-1]#it prints only the last character of the name
    last_character=name[-2] #it prints the second last , and so on and so on 

    print(name)
    print(first_name)
    print(last_name)
    print(last_character)

