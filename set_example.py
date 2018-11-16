# coding=utf-8

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)    

# use & operator
# Output: {4, 5}
print(A & B)

# use - operator on A
# Output: {1, 2, 3}
print(A - B)