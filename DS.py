#DS representing data in structured way is called data structure.

# a = 12,13,14,15

# print(a)
# print(type(a))

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

num = [12,34,53,67,84,21]

lar = num[0]
# sec_lar = num[2]

for i in range(len(num)):
    if num[i] > lar:
        lar = num[i]

print(lar)


print(f"greates number in the list is : {gratest}")


4. Find the second greatest element?


num = [12, 34, 53, 67, 84, 21]

lar = num[0]
index = 0
sec_lar = float('-inf')  
sec_lar_index = -1  

for i in range(len(num)):
    if num[i] > lar:
        sec_lar = lar  
        sec_lar_index = index 
        lar = num[i]
        index = i
    
    elif num[i] > sec_lar and num[i] != lar: 
        sec_lar = num[i]
        sec_lar_index = i

print(f"The largest number is: {lar}, which is at position: {index}")
print(f"The second largest number is: {sec_lar}, which is at position: {sec_lar_index}")


5. Check if List is sorted or not.


num = [1,2,3,4,5]

count = 0


for i in range(len(num)-1):
    if num[i] < num[i+1]:
        continue
    else :
        print("not sorted : ")
        break
    
else :
    print("sorted")


"""
