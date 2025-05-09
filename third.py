# Input and output

# input() # to take input

#

"""name = "Rishi"
age = 18
print( name,age ) #to shoe output


# raw string
print("Hello my name is ", name , "My age is : ", age)

#formatted string

print(f"my name is {name} and I am {age} year old.")

"""
# if else questions
"""a = int( input("Enter first number : ") )
b = int( input("Enter Second number : "))

if(a > b) : 
    print("A is bigger ")
else :
    print("B is bigger ")

if(a % 2 == 0) : 
    print("A is even ")
else :
    print("A is odd ")


name = input("Enter your name ")
age = int( input("Enter your age "))

if (age >= 18) :
    print(f"{name} you can vote ")
else : 
    print("you cant vote")


year = int(input("Enter year "))

if(year % 4 ==0 and year % 400 == 0 and year % 100 == 0) :
    print ("leap")
else :
    print ("not a leap")"""

# if elf ledder

temprature = int(input("Enter the temprature : "))

print(f" this is your temprature {temprature} celcius based on which the whether condition is : ")

if temprature > 40 :
    print("Very Hot 🐦‍🔥")
elif temprature >= 30 and temprature <= 40 :
    print(" Hot 🔥")
elif temprature >= 20 and temprature < 30 :
    print(" plesant 🌥️")
elif temprature >= 10 and temprature < 20 :
    print("Cold 🤧")
elif temprature >= 0 and temprature < 10 :
    print("very Cold 🥶")
else :
    print("Freezing Cold ❄️")
