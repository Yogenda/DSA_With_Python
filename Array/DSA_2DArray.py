import numpy as np

twoDimArray = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(twoDimArray)
'''
print("-----------------------------------")
newTwoDArray = np.insert(twoDimArray,0,[1,2,3],axis=1)
print(newTwoDArray)
print("-----------------------------------")
newTwoDArray = np.append(twoDimArray,[[1,2,3]],axis=0)
print(newTwoDArray)
'''
'''
2d Arrays: 
    m = col
    n = row
TC: O(m,n)
SC: O(m,n)


axis = 1 (col)
axis = 0 (row)
'''

#accessing the 2D array
'''
in 2d array if you are accessing the values then arr[row][col]
'''
'''
def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >=len(array[0]):
        print('Incorrect index')
    else:
        print(array[rowIndex][colIndex])
    #TC: O(1)
    #SC: O(1)
accessElements(twoDimArray,2,1)
'''
'''
#Traversing the 2d Arrray
def traversTwoDArray(array):
    for i in range(len(array)):         #O(mn)
        for j in range(len(array[0])):  #O(n)
            print(array[i],[j])         #O(1)
    #TC: O(n^2)
    #SC: O(1)      

traversTwoDArray(twoDimArray)
'''
'''
print('-------------------------------')
#delete value in 2d array
newDelArray = np.delete(twoDimArray,1,axis=1)
print(newDelArray)
#TC: O(mn)
#SC: O(mn)
'''

'''
time and space complexity of 2d Array

Operation                               TC      SC
create an empty array                   O(1)    O(1)
create an array with values             O(mn)   O(mn)
insert the column/row in array          O(mn)   O(mn)
traversing a given array                O(mn)   O(1)
accessing a given cell                  O(1)    O(1)
searching a given value                 O(mn)   O(1)
delete a col/row                        O(mn)   O(mn)


'''


    