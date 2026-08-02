
import numpy as np

# make zeros array

zeros = np.zeros((2,3), dtype=int)
print(zeros)
print(zeros.ndim)
print(zeros.dtype)
print(zeros.shape)
print(zeros.size)

#make ones array

ones = np.ones((3,3))

print(ones)
print(ones.ndim)
print(ones.dtype)
print(ones.shape)
print(ones.size)


#make eye array or identity array

identity_matrix = np.eye(4, dtype=int)

print(identity_matrix)
print(identity_matrix.ndim)
print(identity_matrix.dtype)
print(identity_matrix.shape)
print(identity_matrix.size)


#make arange array

arange = np.arange(1,20,2)

print(arange)
print(arange.ndim)
print(arange.dtype)
print(arange.shape)
print(arange.size)

# make linspace array

linspace = np.linspace(1,2,5)

print(linspace)
print(linspace.ndim)
print(linspace.dtype)
print(linspace.shape)
print(linspace.size)


# practice task
# 1 3X3 zero array

task_1 = np.zeros((3,3))
print(task_1)

# 2 even number ( 1 to 20)

task_2 = np.arange(2,21,2)
print(task_2)

# divided (0 to 1) in 5

task_3 = np.linspace(0,1,5)
print(task_3)