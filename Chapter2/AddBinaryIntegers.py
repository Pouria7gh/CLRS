A = [1, 0, 1, 0, 1, 1]
B = [1, 1, 1, 0, 0, 1]
n = len(A)

carry = [0]
C = []

for i in range(n) :
    total = A[i] + B[i] + carry[i]
    carry.append(total // 2)
    C.append(total % 2)

C.append(carry[-1])
print(C)