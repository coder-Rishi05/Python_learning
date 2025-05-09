# conditionals

def number(): 
        
        a = int(input("Enter first number : ")) 
        b = int(input("Enter Second number : ")) 

        if a > b :
            print("first is bigger then second")
        elif b > a :
            print(" second is bigger then first")
        else : 
            print('nothing')

# number()

def gender():

        c = input("Enter your gender : (Male/Female) ")

        if c == "Male" :
            print(f'Hello {c} Friend : ')
        elif c == "Female" : 
            print(f'Hello {c} Friend : ')
        else :
            print("Enter a gender only : ")

gender()

# for web scrapping in pythin we use Beutiful soup.
