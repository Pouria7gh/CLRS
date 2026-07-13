A = [5, 2, 4, 6, 1, 3]
n = len(A)

for i in range(1, n) :
    key = A[i]
    j = i - 1
    while j >= 0 and key < A[j] :
        A[j + 1] = A[j]
        j = j - 1
    A[j + 1] = key

print(A)