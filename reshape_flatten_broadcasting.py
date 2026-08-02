import numpy as np 

# reshape 
a = np.array([[2,4,5],[9,5,6]])

print(a)
b = (a.flatten())

print(b)

c = b.reshape(2,3)

print(c) 

d = c.reshape(3, -1)

print(d)

print(np.sum(d, axis=0))
print(np.sum(d, axis=1))

# broadcasting
x = np.array([1,2,3,5,6,7,8,9])

print(x + 5)

print(x *  3)

print(x - 11)

b = np.array([[1],[4],[7]])
c = np.array([11, 23, 40, 50, 79])

print(b + c)

print(b * c)


task_1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print(task_1.reshape(4,3))

task_2 = np.array([5,10,15])

print(task_2 + 100)
