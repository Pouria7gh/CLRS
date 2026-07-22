def recursive_insertion_sort(A, n) :
    if n <= 1 : return

    recursive_insertion_sort(A, n-1)

    key = A[n-1]
    i = n-2
    while i >= 0 and key < A[i] :
        A[i+1] = A[i]
        i -= 1
    A[i+1] = key

A = [6, 5, 4, 3, 2, 1]

recursive_insertion_sort(A, len(A))
print(A)