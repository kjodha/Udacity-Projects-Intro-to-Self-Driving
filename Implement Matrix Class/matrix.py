import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            return self.g[0][0]
        elif self.h == 2:
            return self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0]
        

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace = 0
        for i in range(self.h):
            for j in range (self.w):
                if(i==j):
                    trace= trace + self.g[i][j]
                else:
                    trace = trace
        return trace

#     def inverse(self):
#         """
#         Calculates the inverse of a 1x1 or 2x2 Matrix.
#         """
#         if not self.is_square():
#             raise(ValueError, "Non-square Matrix does not have an inverse.")
#         if self.h > 2:
#             raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

#         # TODO - your code here
#         inverse=[]
#         if self.h == 1:
#             inverse.append([1 / self.g[0][0]])
#         elif self.h == 2:
#             if (Matrix.determinant(self)==0):
#                 raise ValueError('The matrix is not invertible.')
#             else:
#                 a = self.g[0][0]
#                 b = self.g[0][1]
#                 c = self.g[1][0]
#                 d = self.g[1][1]

#                 factor = 1 / (a * d - b * c)

#                 inverse = [[d, -b],[-c, a]]

#                 for i in range(len(inverse)):
#                     for j in range(len(inverse[0])):
#                         inverse[i][j] = factor * inverse[i][j]
    
#         return Matrix(inverse)


    def identity_matrix(n):

        identity = []

        # TODO: Write a nested for loop to iterate over the rows and
        # columns of the identity matrix. Remember that identity
        # matrices are square so they have the same number of rows
        # and columns
        for i in range(n):
            row=[]
            for j in range(n):
                if(i==j):
                    row.append(1)
                else:
                    row.append(0)
            identity.append(row)
        # Make sure to assign 1 to the diagonal values and 0 everywhere
        # else
        return Matrix(identity)
    
    
    def inverse(self):

        inverse = []

        if self.h != self.w:
            raise ValueError('The matrix must be square')

        ## TODO: Check if matrix is larger than 2x2.
        ## If matrix is too large, then raise an error
        if (self.h>2):
            raise NotImplementedError('Matrix dimensions are greater than 2, this functionality is not implemented')

        ## TODO: Check if matrix is 1x1 or 2x2.
        if (self.h==1):
            for i in range(self.h):
                row=[]
                val = 1 / self.g[i][0]
                row.append(val)
            inverse.append(row)
        else:
            det=0
            ad=1
            bc=1
            trace=0
            for i in range(self.h):
                row=[]
                for j in range(self.w):
                    if(i==j):
                        ad=ad*self.g[i][j]
                        trace = trace + self.g[i][j]
                    else:
                        bc=bc*self.g[i][j]
            det=ad-bc
            if(det==0):
                raise ValueError('The matrix is not invertible')
            else:
                identity=[]
                identity=Matrix.identity_matrix(self.h)
                tr_Identity = []
                for i in range(identity.h):
                    row=[]
                    for j in range(identity.w):
                        val = identity.g[i][j]*trace
                        row.append(val)
                    tr_Identity.append(row)
                Bracket=[]
                for i in range(len(tr_Identity)):
                    row=[]
                    for j in range(len(tr_Identity[0])):
                        val = tr_Identity[i][j]-self.g[i][j]
                        row.append(val)
                    Bracket.append(row)
                for i in range(len(Bracket)):
                    row=[]
                    for j in range(len(Bracket[0])):
                        val =  Bracket[i][j]/det
                        row.append(val)
                    inverse.append(row)
        return Matrix(inverse)


    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        for i in range(self.w):
            row=[]
            for j in range(self.h):
                row.append(self.g[j][i])
            matrix_transpose.append(row)
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        Sum=[]
        for i in range(self.h):
            row=[]
            for j in range(self.w):
                val = self.g[i][j] + other.g[i][j]
                row.append(val)
            Sum.append(row)
        return Matrix(Sum)
               
            

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        Neg=[]
        for i in range(self.h):
            row=[]
            for j in range(self.w):
                val = - self.g[i][j]
                row.append(val)
            Neg.append(row)
        return Matrix(Neg)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        Sub=[]
        for i in range(self.h):
            row=[]
            for j in range(self.w):
                val = self.g[i][j] - other.g[i][j]
                row.append(val)
            Sub.append(row)
        return Matrix(Sub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        mul = zeroes(self.h, other.w)
        
        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):
                    mul[i][j] = mul[i][j] + self.g[i][k] * other.g[k][j]
        return mul
        

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            grid = self
            for i in range(self.h):
                for j in range(self.w):
                    grid[i][j] *= other
            return grid
       
            
            