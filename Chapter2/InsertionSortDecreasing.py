A = [41, 59, 26, 41, 58]
n = len(A)

for i in range(1, n) :
    key = A[i]
    j = i - 1
    while j >=0 and key > A[j] :
        A[j + 1] = A[j]
        j = j - 1
    A[j + 1] = key

print(A)