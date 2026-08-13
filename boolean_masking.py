

import numpy as np 


students_marks = np.array([70,80,90,23,50,32,78,16,70,85,90,33,30,45,50,60,47])

# print(students_marks) 

a= students_marks

# print(a[a>40])

# print(max(a))

# print(a[(a > 40) & (a > 20)])

# print(a > 40 )

print("Passed Students:", a[a >= 33])

print("Failed Students:", a[a < 33])

b = max(a)

print( "Top Marks Of Students:", b)

print( "Top Marks Of Students:", a[a >= 90])
