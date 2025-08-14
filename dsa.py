# a = [1,2,1,1,1,2,2,2]

# dict = {}

# for i in a:
#         if i in dict.keys():
#             dict[i] += 1
#         else:
#             dict[i] = 1	

# print(dict)

"""

1. Find the smallest.
2. substract the smallest from the whole array.
3. choose a new smallest.
4. Again substarct from the whole array till the whole array become 0.
5. return number of operations to make it 0.
"""

# b = [1,2,3,2,5,6]

# count = 0

# s = b[0]

# sum_o_a = 0

# for i in range(len(b)):
#     #  sum_o_a = sum_o_a + b[i]
#     #  while sum_o_a != 0:
#         if(s > 0 & s > b[i]):
#             s = b[i]
#         for i in range(len(b)):
#             b[i] -= s
        #    sum_o_a = sum_o_a + b[i]



# print(f"Smallest number in the array is : {b}")
"""
logic for checking whether my array have 0s in all index or not.


a = [1,2,1,4]

a1 = [0,0,0,0]
sum_o_a = 0
c = 0

length = len(a)

for i in range(length):
    # if(a[i] == 0):
       sum_o_a = sum_o_a + a1[i]

print(sum_o_a)

"""

"""
set way

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        positives = []
        for i in nums:
            if i > 0:
                positives.append(i)

        unique = set(positives)
        return len(unique)

"""

nums = [6,6,5,5,4,1,6]

arr = [nums[0]]

for i in nums[1:]:
     if i != arr[-1]:
          arr.append(i)

print(arr)

"""class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        arr = [nums[0]]
        for i in nums[1:]:
             if i != arr[-1]:
                 arr.append(i)
    
        count = 0

        for i in range(1,len(arr)-1):
            if(arr[i] > arr[i-1] and arr[i] > arr[i+1] or arr[i] < arr[i-1] and arr[i] < arr[i+1] ):
                count +=1
        return count"""