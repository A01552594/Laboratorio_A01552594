import numpy as np


A = np.array ([[1,2,3],
              [4,5,6],
              [7,8,9]])

B = np.array ([[9,8,7],
              [6,5,4],
              [3,2,1]])


A_row, A_col = A.shape
B_row, B_col = B.shape 
result = 0.0
for row in range(A_row):
  for col in range(A_col):
      result += A[row,col] *  B[row,col]


print(A*B)
print(result)