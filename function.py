"""
Functions in Python group reusable code into a block that can be executed by calling the function name. This helps
avoid repetition and makes programs modular and readable. There are many in-build functions in python like 
    print(),
    input()
    len() etc.

"""

# to find sum


def sum(a,b):
    return a + b

print(sum(12,45))

# to greet with default values and without default value

def greet(name="Rishi"):
    print(f"Heloo {name}")

greet() #without defualt value
greet("Rishabh") # with default value


# key word argument function

def intro(name,age):
    print(f"your name is {name} and age is {age}  ")

intro(age = 12, name="Akash")





def pali(word):
    rev = ""
    for i in (range(len(word)-1,-1,-1)):
        rev = rev + word[i]
    if(rev==word) : 
        print(f" {word} palindrome")
    else:
        print(f" {word} not a palindrome : ")    

pali("naman")
pali("bali")


# return print or return the values.

def hello():
    return "hey"

print(hello())