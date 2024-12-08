
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

arr2 = np.array(2,34,52,37,82,55,45,36,47,84,22,42)
arr3 = arr2.reshape(3,4)
print(arr3)