
a = range(16,0,-1) # for reverse
b = range(-5,-16,-1) # for negatives
c = range(5,51,5) # for table

n = int(input("Enter number for table : "))
a = 1
# for i in range(s,s,s):
for i in range(n,(n*10)+1,n):
    # print(f" {n} * {a} :  ",  i, sep="~")
    print(f" {n} * {a} : ", i)
    a = a+ 1
''
''
''
''


sum1 = 1

# def fact(n):
#     if n == 0: return
#     sum1 *= n
#     print(sum1)
#     fact(n-1)


# fact(5)

# for i in range(1,5,1):
#     sum1 = sum1 * i


# print(sum1)