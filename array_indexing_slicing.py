
import numpy as np

# 1D array indexing and slicing 

a = np.array([1,2,3,4,5,6,7])

# indexing
print(a)
print(a[2])
print(a[5])
print(a[-3])

# slicing
print(a[:2])
print(a[2:5])
print(a[:6])
print(a[0:5:2]) # step slicing, 0 start, 5 stop, 2 step

# 2D array indexing and slicing

b = np.array([[1,2,3], [4,5,6]])
print(b)
# indexing
print(b[1,2])
print(b[-1,-2])

# slicing

# print(b[1:2, 2:3])
print(b[0:1, 1:2])

task_1 = np.array([[7,8,9],[4,5,6]])

print(task_1[0:1, 1:2])

print(task_1[1:3, 2:3])

print(task_1[1:2,1:2 ])

print(task_1[0:1, 2:3])


c = np.random.randint(1,10,size=(3,3))
print(c)

d = np.random.randint(1,10,size=(2,3,3))
print(d)