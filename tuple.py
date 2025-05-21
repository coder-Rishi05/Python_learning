# Tupple in Data Structures : 


# Immutable - Tuples are not mutable you cannot change the values of tuple.
# Duplicates - You can have duplicate values in tuple there are no restriction.
# Ordered - Set are ordered and you can access them through index values.
# Heterogenous - Set also have heterogenous nature and can have different types of data structure in tuple.


# it can store string and functions both. 
a = (1,23,4,2,3,3,1,3,3,print(),"hello")

#traversing in tuple

for i in range(len(a)) :
    print(i-2)

# methods of tuple

index = a.index(print( ))
count = a.count(3)
print(index)
print(count)

# touple unpacking 

a = (10,11,12,13,14)

# if i want to assing the above vlues to multiple variables then i can do this

a,b,c,d,e = a

print(f" the value of a is {a}")
print(f" the value of b is {b}")
print(f" the value of c is {c}")
print(f" the value of d is {d}")
print(f" the value of e is {e}")

print('this is called tuple unpacking')

# important thing about touple

x = (1) #this is not touple as it is unpacked so it's type is int.

# to make it touple we can write 

x = (1,) # now it is touple.


