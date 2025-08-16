""" 
Python question revisions. 

Stage 1: Beginner Basics (Syntax & Variables)

            1.Print "Hello, Python!"

            2.Store your name in a variable and print: "Hello, <name>!".

            3.Swap the values of two variables without using a third variable.

            4.Convert a number into a string and print its type.

            5.Take a number from the user and print whether it’s even or odd.

Stage 2: Conditions & Loops

            6.Take a number as input and print "Positive", "Negative", or "Zero".

            7.Print numbers from 1 to 10 using:

            i) for loop

            ii) while loop

            8. Find the sum of the first 50 natural numbers.

            9. Print the multiplication table of a given number.

            10. Print all even numbers between 1 and 100.

Stage 3: Strings

            11. Reverse a string without using slicing ([::-1]).

            12. Count the number of vowels in a string.

            13. Check if a string is a palindrome.

            14. Remove all spaces from a string.

            15. Count how many times each character appears in a string.

Stage 4: Lists, Tuples, and Dictionaries

            Find the largest number in a list.

            Remove duplicates from a list without using set().

            Given two lists, create a new list containing elements present in both.

            Create a dictionary of 5 fruits with their prices and print each item.

            Count the frequency of words in a given sentence.

Stage 5: Functions & Mid-Level Logic

            Write a function to calculate the factorial of a number.

            Write a function to check if a number is prime.

            Create a function that takes a list and returns the second largest number.

            Create a function that takes a list and returns it in reverse order without using .reverse() or slicing.

            Write a function to check if two strings are anagrams.

"""

def stage1():

    print("Stage 1 ...")

    print("Hello world")

    a = "king"

    print(a)

    a1 = 10
    b1 = 12

    print("Numbers before swapped ",a1, b1)
    
    a1 = a1+b1 # 10 + 12 = 22
    b1 = a1-b1 # 22 - 12 = 10
    a1 = a1-b1 # 22 - 10 = 12


    print("Numbers after swapped ",a1, b1)

    c = 12

    print(type(chr(c)), chr(c))

    a = input("Enter a number : ")

    if int(a) % 2 == 0:
        print("Even no.")
    elif int(a) % 2 != 0 :
        print("odd")
    else :
        print("enter a number : ")

    print("Stage 1 cleared ✅")


def stage2():    


    print("Stage 2... ")


    a = input("Enter a number : ")

    if int(a) > 0:
        print("Positive number.")
    elif int(a) < 0 :
        print("Negative number")
    elif int(a) == 0 :
        print(" number is 0 : ")
    else:
        print("Enter a valid number.")

        a1 = 11

        for i in range(1, a1, ):
            print(i)

        s = 1

        while s <= 10:
            print(s)
            s = s+1


        a2 = 50
        sum1 = 0

        for i in range(1,a2):
            sum1 += i

        print(sum1)

        num = input("Enter a number for table")

        for i in range(1,int(num),11):
            print(int(num) * i)

        e = 100

        for i in range(1,e,101):
            if i % 2 ==0:
                print(i)
    print("Stage 2 completed... ✅")


def stage3():
    print("hi")


arr = ["😅","🧑‍💻","⬇️","✅","🚀","🟢","🔴","🔥","😊","❌","😶‍🌫️","💀","👌","👲","🐦‍🔥"]

for i in arr:

    print(f"unicode of this arr{[i]} is : ",ord(i))
    # print()

