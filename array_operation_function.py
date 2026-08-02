
import  numpy as np 
# array operation 
a = np.array([1,2,3,4])
b= np.array([5,6,7,8])
print(a)
print(b)

# operation of array

print( a + b )

print( a - b )

print( a * b )

print( a/ b )

print(a ** 2)

# math functions 

x = np.array([4,5,6,7,8,9,11,12])
print(np.sqrt(x))
print(np.exp(x))
print(np.log(x))
print(np.sin(x))
print(np.cos(x))
print(np.sum(x))
print(np.mean(x))
print(np.median(x))
print(np.max(x))
print(np.min(x))

# statistical functions

print(np.std(x))
print(np.var(x))

# 2D array operation
y = np.array([[1,2,3],[6,7,8]])

print(y)

print(np.sum(y))
print(np.sum(y, axis=0)) #column wise sum 
print(np.sum(y, axis=1)) # row wise sum 
print(np.mean(y))

# task 

task_1 = [10,20,30,40]

print(np.average(task_1))

task_2 = np.random.randint(1,10, size=(2,2))
print(task_2)

print(np.sum(task_2, axis=0))

task_3 = np.array([3,6,9])

print(np.square(task_3))