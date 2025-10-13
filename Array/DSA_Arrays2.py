import array

import numpy as np
'''

my_array = array.array('i')     #O(1)
print(my_array)
my_array = array.array('i',[1,2,3,4,5])   #O(1)
print(my_array)



np_array = np.array([],dtype=int)    #O(N)
print(np_array)
np_array = np.array([1,2,3,4,5,'a'])     #O(N)
print(np_array)
'''

my_array = array.array('i',[1,2,3,4,5,6])
print(my_array)
# my_array.insert(0,7)
# print(my_array)
# TC: O(n)
# SC: O(1)

# my_array.insert(3,7)
# print(my_array)

# my_array.insert(7,7)
# print(my_array)

from array import *
#Traversing the array values
arr1=array('i',[1,2,3,4,5,6])
arr2= array('d',[1.2,2.5,3.6])
print(arr1)
# arr2[3]
print(arr2)

def traversArray(array):
    for i in array:    #TC:  O(N)
        print(i)       #TC:  O(1)

#TC: O(n)
#SC: O(1)

traversArray(arr2)


#How to access an element in array
#Note: if you are accessing the value in +ve index then the direction is left to right
    # if you are accessing the value in -ve index then the direction is right to left
arr1 = array('i',[1,2,3,4,5,6])

def accessElement(array,index):
    if index>=len(array):             #O(1)
        print('There is no such index preset try again....')   #O(1)
    else:
        print(array[index])           #O(1)

# TC: O(1)
# SC: O(1)

accessElement(arr1,6)

