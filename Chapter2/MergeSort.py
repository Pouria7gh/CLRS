def Merge(A, p, q, r) :
    nl = q - p + 1
    nr = r - q
    L = A[p:q+1]
    R = A[q+1:r+1]

    i = 0
    j = 0
    k = p
    while i < nl and j < nr :
        if L[i] <= R[j] :
            A[k] = L[i]
            i = i + 1
        else :
            A[k] = R[j]
            j = j + 1
        k = k + 1

    while i < nl :
        A[k] = L[i]
        i = i + 1
        k = k + 1
    while j < nr :
        A[k] = R[j]
        j = j + 1
        k = k + 1

def MergeSort(A, p, r) :
    if r <= p : return
    q = (p + r) // 2
    MergeSort(A, p, q)
    MergeSort(A, q + 1, r)
    Merge(A, p, q, r)

A = [5, 2, 4, 6, 1, 3]
MergeSort(A, 0, len(A) - 1)
print(A)