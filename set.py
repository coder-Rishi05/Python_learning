'''
sets : 

mutable - Sets are mutable you can change the values of set
Duplicates - You cannot have any duplicate values in set that means every element will be uniqueO
Unordered - Sets are unordered and you cannot access them through index values
Heterogenous - Set is semi-heterogenous it can store some data types like string, numbers,tuples but not everything
such as functions.
'''

''' 
sets are stored in unorder place there is no index in it.  

sets are stored using hash functions.
hash used as index
only immutable objects such as number,string and tuple are allowed in set to store.
Immutable objects such as number string and tuples are not allowed.

'''

s = {1,2,3,4,5}



b = (1,2,3,5,2)

print(hash('A')) # its a hash value of char a => 3666365078521613816 it is changing on every run

print(hash(b)) # its a hash value of tuple b => 6625964432961385851 it is fixed

# beacasue of this sets are immutable

# print(s)


#set traversing :


s1 = {1,"hello",8,7,2,3,4,5}



#in case of integer the set will be printed in sorting order casuse integer hash value saved in the way that they show in numbers. its also depen on the ram of ones pc.

"""

Methods in sets

set1 = {12,13,5,63,2,56}

set1.add(10)
set1.remove(12) # remove the element
# set1.remove(101) # error as it is not in the set
set1.discard(12) # it will also remove the element but will not give error if element not found.

pop_element = set1.pop() #remove a random element.


set1.clear() # remove all the set elements

for i in set1:
    print(i)


# for i in s1:
#     print(i)

print(pop_element)


"""

"""

Special sets methods to perform between two sets.

1. union => 

first_set = {12,13,14,11,35}
second_set = {1,12,13,14,11}

union_set = first_set.union(second_set) # union method
# it will print only unique elements from both sets.

print(union_set)

print(first_set)
print(second_set)

print(first_set | second_set) # union symbol

first_set = {12,13,14,11,35}
second_set = {1,12,13,14,11}

union_set = first_set.union(second_set) # union method
# it will print only unique elements from both sets.

print(union_set)

print(first_set)
print(second_set)

print(first_set | second_set) # union symbol


2. Intersection

a = {1,2,3,4,5}
b = {4,5,6,7,8}

print(a)
print(b)

#  Intersection method

s = a.intersection(b)
print(s)

#  Intersection symbol

s1 = a&b

print(s1)


3. Diffrence



a = {1,2,3,4,5}
b = {4,5,6,7,8}


print(a)
print(b)

#  diffrence method

s = a.difference(b)
print(s)

#  diffrence symbol

s1 = a-b

# or

s2 = b - a


print(s2)
print(s1)


# 4. Symetric Diffrence



a = {1,2,3,4,5}
b = {4,5,6,7,8}


print(a)
print(b)

# symmetric diffrence

s1 = a.symmetric_difference(b)

print(s1)

# symmetric symbol

s = b ^ a 
print(s)


2. Intersection

a = {1,2,3,4,5}
b = {4,5,6,7,8}

print(a)
print(b)

#  Intersection method

s = a.intersection(b)
print(s)

#  Intersection symbol

s1 = a&b

print(s1)


3. Diffrence



a = {1,2,3,4,5}
b = {4,5,6,7,8}


print(a)
print(b)

#  diffrence method

s = a.difference(b)
print(s)

#  diffrence symbol

s1 = a-b

# or

s2 = b - a


print(s2)
print(s1)



# 4. Symetric Diffrence



a = {1,2,3,4,5}
b = {4,5,6,7,8}


print(a)
print(b)

# symmetric diffrence

s1 = a.symmetric_difference(b)

print(s1)

# symmetric symbol

s = b ^ a 
print(s)
"""

