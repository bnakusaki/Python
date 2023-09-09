# Python arrays
import array as arr

"""
typecode -- type -- minsize in bytes
b -- int -- 1
u -- unicode character -- 2
i -- int -- 2
l -- int -- 4
q -- int -- 8
f -- float -- 4
d -- float -- 8
"""
a = arr.array('i', [1,2,3,4,5,6,7,8,9]) # integers min 2

"""Arrays work basically as lists work, insertion, iterations, deletion
slicing and many more"""

# To access all available typecodes
print(arr.typecodes)

# To access the actual size of the array elements
print(a.itemsize)

# Iterations
# for x in range(len(a)):
#    print(x, end=' ')

#print()

# Insertions
a.insert(1, 0)
#print(a)

# Deletion
del a[1]
#print(a)

# Slicing
b = a[:]
#print(b)

del a[0]
#print(a.itemsize)
#print(b)