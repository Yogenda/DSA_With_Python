from array import *

#arr = array('i',[1,2,3,4,5,6])
'''
def arrayAccess(array, index):
    if index>len(array):
        print('There is no such element in this position...')
    else:
        print(array[index])

# TC: O(1)
# SC: O(1)
arrayAccess(arr,3)
arrayAccess(arr,8)
'''
'''
def searchValue(array, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

print(searchValue(arr, 4))
print(searchValue(arr, 6))
print(searchValue(arr, 10))
'''    
'''
print(arr)
arr.remove(2)
print(arr)
arr.remove(5)
print(arr)
'''

'''
Array TC and SC
Operation                       TC              SC
creat an empty array            O(1)            O(1)
create an array with element    O(n)            O(n)
insert the value in array       O(n)            O(1)
Traversing the array            O(n)            O(1)
Access a given cell             O(1)            O(1)
Search a given element          O(n)            O(1)
Delete a given value            O(n)            O(1)
'''

#Create an array and traverse.
my_array = array('i',[10,20,30,40,50,60])
'''
for i in my_array:
    print(i)
'''

#  access an individual element trouugh index
print(my_array[2])

'''
HW python
- append an value to the array using the append() method
- Insert the value in array using the insert() method
- Extend the array by using the extend() method.
- add the item from the array using the fromlist() method.
- remove an element from array using the remove() mehtod.
- Remove a last element from array using the pop() method.
- fetch an element through its index using index() method.
- reverse the array by using the reverse() method.
- check the number of occurance of an element in array using count() method.
- convert the array to string using the tostring() method.
- slice an element from an array.

'''
