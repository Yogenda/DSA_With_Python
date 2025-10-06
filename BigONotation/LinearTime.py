def printValues(n):
    for i in range(n):  #----------- O(n)
        print(i)
    for j in range(n):  #----------- O(n)
        print(j)
        
printValues(5)

#O(n)+O(N) = O(2N) = O(N)