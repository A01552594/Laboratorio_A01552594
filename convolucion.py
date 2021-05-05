import numpy as np

def conv_helper(fragment, kernel):
    
    f_row, f_col = fragment.shape
    result = 0
    for row in range(f_row):
        for col in range(f_col):
            result += fragment[row,col] *  kernel[row,col]
    return result



image = np.array ([[1,2,3,4,5,6],
              [7,8,9,10,11,12],
              [0,0,1,16,17,18],
              [0,1,0,7,23,24],
              [1,7,6,5,4,3]])

kernel = np.array ([[1,1,1],
              [0,0,0],
              [2,10,3]])


image_row, image_col = image.shape 
kernel_row, kernel_col = kernel.shape


outputy=int(image_col-(kernel_col/2)*2+1)
outputx=int(image_row-(kernel_row/2)*2+1)

output = np.zeros((outputx,outputy))


   
for row in range(outputx):
    for col in range(outputy):
            output[row, col] = conv_helper(
                                image[row:row + kernel_row, 
                                col:col + kernel_col],kernel)


print(output)




