def printValues(n):
    for i in range(n):   #-----------O(n)
        for j in range(n): #-----------O(n)
            print(i,j)

printValues(5)

# n*n = O(n^2)

def printValues(n):
    for i in range(n):   #-----------O(n)
        for j in range(n): #-----------O(n)
            for k in range(n): #-----------O(n)
                print(i,j,k)

printValues(5)

# n*n* = O(n^3)