"""For and range function"""

range(1,20,2) #range accept 3s => start, stop, steps it is used in for loop.

# a = range(1,21,1) ! range have default value 0 for start, stop is given by user, steps is by default 1.

for i in range(-5,-16,-1) : # for reverse print step will be in -1.
    print("hey", i)


    # table of 5

# for i in range(1,11,1) :
#     print(5 * i)

# for i in range(7,71,7) :
#     print(i)

# """ loops using string """

# a = "Rishabh"

# for i in range(len(a)) :
#     print(a[i])

    # we can also use else break and continue in loop

# for loop practice questions.

"""
1. Accept an integer and Print hello world n time
    a = int(input("Enter a number : "))
    for i in range(a) :
        print("Hello")
2. Print natural number up to n
a = int(input("Enter a number : "))
for i in range(a,a+1) :
    print(i)
3. Reverse for loop. Print n to 1
a = int(input("Enter a number : "))
for i in range(a,0,-1) :
    print(i)
4. Take a number as input and print its table.
a = int(input("Enter a number : "))
for i in range(1,11) :
    print(i*a)
5. Sum up to n terms
    a = int(input("Enter a number : "))
    s = 0
    for i in range(a) :
        s += a
        
    print(s)
6. Factorial of a number
    a = int(input("Enter a number : "))
    su = 1
    for i in range(1,a+1,1) :
    su *= i  
    print(su)
7. Print the sum of all even & odd numbers in a range separately
    a = int(input("Enter a number : "))
    esum = 0
    osum = 0
    for i in range(1,a+1,1) :
        if(i%2==0) :
        esum += i
        elif(i%2 != 0):
        osum += i 
print(f"sum of even number : {esum}")
print(f"sum of odd number : {osum}")
8. Print all the factors of a number
    a = int(input("Enter a number which factor you want to know : "))
    
    for i in range(1,a+1,1):
        if(a%i==0):
        print(i)
        
9. Accept a number and check if it a perfect number or not.
 A number whose sum of factors is equal to the number itself
 Ex - 6 = 1, 2, 3 = 6
 a = int(input("Enter a number : "))
    su = 0
    for i in range(1,a):
        if(a%i==0):
        su += i
        
    if(su == a):
        print(f"This is a perfect number {a} ")
    else:
        print(f" {a} is not a perfect number : ")
    
10. Check wether the number is prime or not.
    a = int(input("Enter a number to count its factor : "))
    count = 0
    for i in range(1,a+1):
        if(a%i==0):
            print(i)
            count+=1
    if(count > 2) :
        print("Not prime")
    else:
        print("prime")
    print(count)
    
11. Reverse a string without using in build functions.
a = input("Enter a string : ")
    b = ""
    print(a)
    for i in range(len(a)-1,-1,-1):
        print(a[i]) 
        b = b+a[i]
    
    print(b)
12. Check string is Pallindrome or not.
    
a = input("Enter your string : ")
    b = ""
    for i in range(len(a-1),-1,-1):
        b = b + a[i]
    if b == a :
        print("palindrome")
    else:
        print("not a palindrome")
13 Count all letters, digits, and special symbols from a given
string
 Given: str1 = "P@#yn26at^&i5ve"
 Expected Outcome:
 Total counts of chars, digits, and symbols
 Chars = 8
 Digits = 3
 Symbol = 4

 ans. 
        
a = "P@#yn26at^&i5ve"

        char = 0
        dig = 0
        sp_char = 0

        for i in a :
            if i.isdigit():
                dig += 1
            elif i.isalpha():
                char += 1
            else :
                sp_char += 1

        print(char)
        print(dig)
        print(sp_char)

"""




"""While

1. Separate each digit of a number and print it on the new line.

    a = int(input("Enter you digit : "))

    seprate_digit = 0
    su = 0
    while a != 0 :
    
    seprate_digit =  a%10
    su = (su * 10) + seprate_digit
    a = a//10


    print(su)
    

2. Accept a number and print its reverse.

a = int(input("Enter a number : "))
# a =123
n_um = 0
rev = 0

while a != 0 :
    n_um =  a % 10
    rev = (rev * 10) + n_um
    a =  a // 10

print(f"reverse of the given number : {rev} ")

3. Accept a number and check if it is a pallindromic number (If
    number and its reverse are equal?

    
a = int(input("Enter a number : "))
# a =123
n_um = 0
rev = 0
b = a

while a != 0 :
    n_um =  a % 10
    rev = (rev * 10) + n_um
    a =  a // 10

if rev != b :
    print("Not a palinfrome : ")
else : 
    print("It's a palindrome number : ")

4. Create a random number guessing game with python.



"""

import random

a = random.randint(1,20)


b = int(input("Enter your guess you have three tries : "))

# if  :
#     print("Your guess is right : 👌 \n")
# elif :
#     print(f"Your guess is wrong : try again {a}")    

