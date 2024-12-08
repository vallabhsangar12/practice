
import random
import numpy as np

arr = np.array([1,5,6,7,9])
print("Array:",arr)

#check numpy version
print(np.__version__)

#print arr type
print(type(arr))

#use of tuple to create ndarray
ar = np.array((4,6,8,4,2))
print("ndarray:",ar)

#0-D array
zero = np.array(23)   
print("0-D array:",zero)

#2-D array
two_d = np.array([23,43,56],[56,78,98])
print("2D array:",two_d)

#Create a 3-D array 
three_d = np.array([23,45,67],[34,64,23],[5,44,56,33])
print("3D Array:",three_d)

#check dimension of array
print(zero.ndim)
print(two_d.ndim)
print(three_d.ndim)

#access array elements
print(ar[0])

#access 2d array
print(two_d([1,3]))

#access 3d array
print(three_d[1, 0, 1])
print(three_d[2]+three_d[3])

#Slicing arrays
print(arr[1:3])
print(arr[3:])
print(arr[:4])
print(arr[-3:-1])
print(arr[0:2, 1:2])
print(two_d.shape)

#shape and reshape
arr2 = np.array(2,34,52,37,82,55,45,36,47,84,22,42)
arr3 = arr2.reshape(3,4)
print(arr3)

#iterating array
for x in arr:
    print(x)

#iterating 2D array
td = np.array([[2,3,4],[5,6,7]])
for x in td:
   for y in x:
    print(y)

#array join
a = np.array([1,2,3])
b = np.array([5,6,7])
c = np.concatenate((a,b))
print(c)

#join with stack function
d = np.stack((a,b), axis=1)

#array split
newarr = np.array_split(arr2, 3)
print(newarr)

#Split Into Arrays

arr5 = np.array([1, 2, 3, 4, 5, 6])

newar = np.array_split(arr, 3)

print(newar[0])
print(newar[1])
print(newar[2])

# arr seach
x = np.where(arr == 4)
print(x)

x = np.where(arr%2 == 0)

print(x)

x = np.searchsorted(arr, 7)

print(x)

#sort arr
print(np.sort(arr))

#arr filter
array1 = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarrr = arr[x]
print(newarrr)

#filtering ex
# Create an empty list
filter_arr = []

# go through each element in arr
for element in array1:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = array1[filter_arr]

print(filter_arr)
print(newarr)

#random function
x = random.randint(100)
print(x)

x = random.rand()

print(x)

x=random.randint(100, size=(5))

print(x)

#random distribution
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)

#random shuffle
random.shuffle(arr)
print(arr)

#random permutations
arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))

#Universal Functions

#zip function
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
  z.append(i + j)
print(z)

#add functions
z = np.add(x, y)
print(z)

#ARITHMATIC FUNCTION
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

ad = np.add(arr1, arr2)
sub = np.subtract(arr1, arr2)
mul = np.multiply(arr1, arr2)
div = np.divide(arr1, arr2)
mod = np.mod(arr1, arr2)
rem = np.remainder(arr1, arr2)
abs = np.absolute(arr)
print(ad)
print(sub)
print(mul)
print(div)
print(mod)
print(rem)
print(abs)

#logs 
#log2() function
arr = np.arange(1, 10)
print(np.log2(arr))

#log at any base
nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))

#sum values in arr1 and arr2
newarr = np.sum([arr1, arr2])
print(newarr)

#product 
array32 = np.array([1, 2, 3, 4])

v = np.prod(array32)

print(v)





