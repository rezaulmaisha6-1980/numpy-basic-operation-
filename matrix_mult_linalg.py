
import numpy as np

a = np.array([[1,2],[7,8]])
b = np.array([[9,4],[5,7]])

c = np.dot(a, b)

print(c)


x = np.random.randint(2,12, size=(3,3))
print(x)

print(np.dot(x,x))

print(a.T)

print(np.linalg.det(a))
print(np.linalg.inv(x))


eigenvalues, eigenvectors = np.linalg.eig(x)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

# solve queations

# 2x + 3y = 5
# 4x + 5y = 6  

A = np.array([[2,3], [4,5]])
B = np.array([5,6])

solution = np.linalg.solve(A, B)
print("Solution:", solution)