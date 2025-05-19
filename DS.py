#DS representing data in structured way is called data structure.

a = 12,13,14,15

print(a)
print(type(a))

# In pyhtin we have 4 types of DS 
"""
1. List
2. Tuple
3. Dictionary
4. Set

# custom DS

1. Stack
2. Queue
3. Linked List
4. Graph
5. Tree

# Algorithms

1. Searching
2. Sorting

"""

#List

"""
Before starting we need to understand some of the terminology.

A - Mutability refers to whether an object's value can be changed after creation. And List allows this.

A - we know data structures are used to store multiple values so duplicates means same value occuring
multiple time. List allows this.

A - List maintains ordered data structure maintains the sequence of elements as they were inserted. This
means you can access elements using their position (index).

A - List have heterogenous nature that means we can have multiple data types inside the list.
"""

# fruits = ["Apple","Banana","Pineapple","Mango","Pomegranate"]

# for i in fruits:
#     print(i)

# fruits[1] = "Grapes"
# print(" \n added grapes in the list \n")
# for i in fruits:
#     print(i)

# print(" \n sorted the list \n")
# fruits.sort()
# for i in fruits:
#     print(i)


"""
list operations


data = [1,2,3,4,5]

data.append(6)
data.insert(1,2)
data.extend([0,12,11])
data.remove(2)
data.sort()
data.reverse()
data.clear()
print(data)

"""


"""
Some questions
1. Print positive and negative elements of an List?


pos_neg_List = [1,2,4,-1,-10,8,-9]

for i in pos_neg_List:
    if(i > 0):
        print(f"positive from the array : {i}")
    elif(i < 0):
        print(f"negative from the array : {i}")

        
2. Mean of List elements?

mean_Data = [1,2,3,1,10,8,19]
mean = 0
count = 0
su = 0
for i in mean_Data :
    count = count + 1
    su = su + i

mean = su // count

print(f"mean of the list is : {mean}")

3. Find the greatest element and print its index too?


mean_Data = [1,2,3,1,10,8,19]
gratest = 0
# count = 0
# su = 0
for i in mean_Data :
    if gratest < i :
        gratest = i


print(f"greates number in the list is : {gratest}")


4. Find the second greatest element?


5. Check if List is sorted or not.

"""



mean_Data = [1,2,3,1,10,8,19]
gratest = 0
index = 0
# count = 1
# su = 0
for i in range(len(mean_Data)) :
    if gratest < mean_Data[i] :
        # count = count + 1
        gratest = mean_Data[i]
        index = i


print(f"greates number in the list is : {gratest}")
print(f"index of greatest element : {index} ")
