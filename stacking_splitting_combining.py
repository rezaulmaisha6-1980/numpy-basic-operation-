

import numpy as np 

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

# add two array with concatenate

x = np.concatenate((a, b))

print(x)

# 2D array concatenate

c = np.array([[1,2,3],[4,5,6]])
d = np.array([[7,8,9],[2,5,7]])

print(np.concatenate((c,d)))
print(np.concatenate((c,d), axis=0))
print(np.concatenate((c,d), axis=1))

#stack 

print(np.vstack((c,d)))
print(np.hstack((c,d)))

# column or row strack

p = np.array([[1,2],[3,4]])
q = np.array([[5,6],[7,8]])

print(np.stack((p,q)))


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

#print(np.row_stack((a,b)))  # row wise
print(np.column_stack((a,b)))  # column wise


names = np.array(["Rohim","Shamim","Korim"])
bangla_marks = np.array([80,90,85])
english_marks = np.array([76,70,84])

marks_table = np.vstack((names,bangla_marks,english_marks))

print("Marks Table:\n", marks_table)

table = np.column_stack((names, bangla_marks, english_marks))

print("Table:\n", table)

# print(np.vstack((marks_table,table)))

# split 

x1 = np.array([1,2,3,4,5,6,7,8])

a, b, c = np.array_split(x1,3)
print(a, b, c)


arr = np.random.rand(2,2)

print(arr)

print(np.vstack(arr))
print(np.hstack(arr))