# Dictionay is also a Data structure. It holds items in keys and values.

"""
Basics 


Mutable - Dictionaries are mutable, meaning you can change, add, or remove key-value pairs after creation.

Duplicates - Keys must be unique, but you can have duplicates in values. 

Order - Dictionary follows insertion order.

Heterogeneous - A dictionary can store different types of keys and values, like integers, strings, lists, or even 
another dictionary.

we can also have string key

"""

d = {1:"hello",2:55, 'hi':'hi', 20:200,}


val = {1:10,2:20,3:30,4:40,5:50,6:60,7:70,8:80}
print(val[2])  # in dictionary key  act as index value to print the actual value.
val[2] = 100
print(val[2])  # we can also change or update the value but cant update keys

val.update({9:20}) # i can also insert  the new value inside my dictionary  using dictionary update method. 

print(val)