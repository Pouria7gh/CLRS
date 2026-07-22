def BinarySearch(v, A, p, r) :
    if p > r: return -1
    
    q = (p + r) // 2

    if A[q] == v:
        return q
    elif A[q] > v :
        return BinarySearch(v, A, p, q-1)
    else:
        return BinarySearch(v, A, q+1, r)

A = [1, 2, 3, 4, 5, 6]
value = 6

key = BinarySearch(value, A, 0, len(A)-1)

print(key)