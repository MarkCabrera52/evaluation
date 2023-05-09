import numpy as np

class MatrixOps:
    def __init__(self, seed=None):
        # We use a predetermined seed to evaluate correct implementation
        if seed:
            np.random.seed(seed)

        self._matrix = np.random.randint(0,10, size=(10,10))
        self._kernel = np.random.randint(-2,2, size=(3,3))
    
    def largest_index(self, matrix):
        ''' Make this function return a tuple of the (row, col) 
            index of the largest value in the matrix '''
        largest = (0,0)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[largest[0]][largest[1]] < matrix[i][j]:
                    largest = (i, j)
        return largest
    
''' scrapped idea
    def get_column(self, matrix, col):   # returns the column of specified matrix
        col_len = len(kernel)
        column = []
        for i in range(col_len):
            column.append(matrix[i][col])
        return column
    
    def flip_first_last_items(self, lst): # flips the first and last values in a list
        last = len(lst) - 1
        new_lst = lst
        new_lst[0] = lst[last]
        new_lst[last] = lst[0]
        return new_lst
'''

    def kernel_inversion(self, kernel):
        # flips kernel along its rows folowed by a flip
        # along its columns
        inversion = kernel
        for i in range(len(kernel)):
            for j in range(len(kernel[0])):
                inversion[j][i] = kernel[i][j]
        return inversion
            

    def convolve(self, kernel, matrix):
        ''' Make this function return the result of a 2D convolution '''
        new_kernel = self.kernel_inversion(kernel)
        # incomplete as I was unsure how to overlap the kernel onto the matrix

        return matrix

    def run(self):
        print("Largest index is at ", self.largest_index(self._matrix))
        
        print("Result of convolution:")
        print(self.convolve(self._kernel, self._matrix))


if __name__ == "__main__":
    # If this file is run directly from the command line, run a test of the program
    m = MatrixOps()


    print("Running with matrix ")
    print(m._matrix)
    print("and kernel ")
    print(m._kernel)

    m.run() 
