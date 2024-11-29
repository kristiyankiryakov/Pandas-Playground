import numpy as np

#1. create 1d array

# array_1d = np.arange(0,11)

#2. create boolean array

# boolean_arr = np.ones(10,dtype=bool)

#3. extract items that satisfy a given condition from 1D array?

# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#4. Replace all odd numbers in arr with -1

# arr[arr % 2 == 1] = -1

#5. Replace all odd numbers in arr with -1 without changing arr

# copied = arr.copy()
# copied[copied % 2 == 1] = -1

#6. Stack arrays a and b vertically

# a = np.arange(10).reshape(2, -1)
# b = np.repeat(1, 10).reshape(2,-1)

# print(np.vstack((a,b)))

#7. Create the following pattern without hardcoding. Use only numpy functions and the below input array a.

# a = np.array([1,2,3])

# Output: array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

# first_part = a.repeat(3)
# second_part = np.tile(a,3)
# result = np.concatenate([first_part, second_part])

# print(result)

#8. Get the common items between a and b

# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])

# Output: array([2, 4])

# common means present in a && b from [a,b]

# print(np.intersect1d(a,b))

#9 From array a remove all items present in array b

# a = np.array([1,2,3,4,5,])
# b = np.array([5,6,7,8,9,2])

# Output: array([1,2,3,4])

# print(np.setdiff1d(a,b))

#10 Get the positions where elements of a and b match

# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])

# Output: (array([1, 3, 5, 7]),)

# print(np.where(a == b))

#11 Get all items between 5 and 10 from a.

# a = np.array([2, 6, 1, 9, 10, 3, 27])

# Output: (array([6, 9, 10]),)

# print(a[(a >= 5) & (a <=10) ])

#15 Convert the function maxx that works on two scalars, to work on two arrays.
# Input:
# def maxx(x, y):
#     """Get the maximum of two items"""
#     if x >= y:
#         return x
#     else:
#         return y
    
# maxx(1, 5)
#> 5

# a = np.array([5, 7, 9, 8, 6, 4, 5])
# b = np.array([6, 3, 4, 8, 9, 7, 1])

# def pair_max(arr1,arr2):
#    result = []
#    result.append(np.max([arr1,arr2], axis=0))
#    return result

# print(pair_max(a,b))

# Output:
# pair_max(a, b)
# array([ 6.,  7.,  9.,  8.,  9.,  7.,  5.])


#16. Swap columns 1 and 2 in the array arr.

# arr = np.arange(9).reshape(3,3)

# print(arr[:, [1,0,2]])

#17. Swap rows 1 and 2 in the array arr:

# print("Original\n", arr)

# print(arr[[1,0,2],:])

#18. Reverse the rows of a 2D array arr.
# arr = np.arange(9).reshape(3,3)

# print(arr)
# print('Original array ===')
# print(arr[::-1,:])

#19. Reverse the columns of a 2D array?




# Questionary
#1.
# arr = np.array([10,20,30,40,50])

# 2.
# (3,2)

# 3.
# np.mean(arr)

# 4.
# arr += 5

# 5.
# third = arr[2]

# 6.
# arr = np.array([[10, 20, 30], 
#                 [40, 50, 60], 
#                 [70, 80, 90]])

#third = arr[1, 1]

# 7.
# first_col = arr[:,0]

#8. the result of arr > 3 will return either arr wil bools for which is true or you can insert it as conditional in the index and get the values for which it applies

#9 not sure

#10. arr.reshape(3,3,3)  again not sure ... also I forgot how to fill values from 0-10 fo e.g
 

# y = np.arange(35).reshape(5, 7)

#20. Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.

# print(np.random.uniform(5,10, size=(5,3)))


a = np.arange(25).reshape(5,5)

divisible = a[a%3==0]

print(divisible)