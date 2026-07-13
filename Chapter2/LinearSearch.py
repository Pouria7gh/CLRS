A = [1, 2, 3, 4, 5, 6]
n = len(A)

x = 5
i = None

for j in range(n) :
    if x == A[j] :
        i = j
        break

print(i)