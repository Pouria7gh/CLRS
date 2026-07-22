def binary_search(A, v) :
    p, r = 0, len(A)-1

    while p <= r :
        q = (p + r) // 2
        
        if A[q] == v :
            return q
        elif A[q] > v:
            r = q-1
        else :
            p = q+1
    
    return -1
    
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
v = 31
key = binary_search(A, v)
print (key)