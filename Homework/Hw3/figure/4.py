import numpy as np
for N in range(1, 7):
    A = np.zeros((4 * N + 2, 4 * N + 2))
    for i in range(4 * N + 2):
        for j in range(4 * N + 2):
            if i % 4 == 0 and j == i + 1:
                A[i, j] = 1
                A[j, i] = 1
            elif j == i - 2 or j == i + 2:
                A[i, j] = 1
    eigenvals = np.linalg.eigvals(A)
    e = np.sort(eigenvals)
    print("N =",4 * N + 2, e[2 * N], e[2 * N + 1])