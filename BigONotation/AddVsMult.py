def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
# tc: O(n+n) = O(N)

# s1
def print_values(a,b): #a=10, b=20
    for i in range(a): # O(a)
        print(i)
    for j in range(b): # O(b)
        print(j)   
    # O(a+b)
    
# s2
def print_values(a,b):
    for i in range(a): # O(a) 5
        for j in range(b): # O(b) 10
            print(i,j) 
    # O(a*b)

    