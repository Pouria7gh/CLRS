A = [41, 59, 26, 41, 58]
n = len(A)

for i in range(n-1) :
    minIndice = i
    for j in range(i + 1, n) :
        if A[minIndice] > A[j] :
            minIndice = j
    A[i], A[minIndice] = A[minIndice], A[i]

print(A)