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

s = {1,21,45,78,3}



b = (1,2,3,5,2)

print(hash('A')) # its a hash value of char a => 3666365078521613816 it is changing on every run

print(hash(b)) # its a hash value of tuple b => 6625964432961385851 it is fixed

# beacasue of this sets are immutable

# print(s)