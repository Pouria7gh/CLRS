def Merge(A, p, q, r) :
    nl = q - p +1
    nr = r - q
    L = A[p: q+1]
    R = A[q+1: r+1]
    
    i = 0
    j = 0
    k = p

    while nl > i and nr > j :
        if L[i] < R[j] :
            A[k] = L[i]
            i += 1
            k += 1
        else :
            A[k] = R[j]
            j += 1
            k += 1
    
    while j < nr:
        A[k] = R[j]
        j += 1
        k += 1
    while i < nl :
        A[k] = L[i]
        i += 1
        k += 1

def Merge_sort(A, p, r) :
    if p >= r : return

    q = (p + r) // 2
    Merge_sort(A, p, q)
    Merge_sort(A, q+1, r)
    Merge(A, p, q, r)


def has_two_sum(A, v) :
    Merge_sort(A, 0, len(A)-1)
    print(A)

    p = 0
    r = len(A)-1
    while p < r :
        current_sum = A[p] + A[r]
        if current_sum == v :
            return (p, r)
        elif current_sum < v :
            p += 1
        else :
            r -= 1

    return None


A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
s = 5
result = has_two_sum(A, s)

print(result)