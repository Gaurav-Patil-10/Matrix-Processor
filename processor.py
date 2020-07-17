
import numpy as np



def inverse (matA):
    mat = matA[:]

    new_mat = np.linalg.inv(mat)

    for x in new_mat:
        for y in x:
            y = float(y)
            y = round(y , 2)

    return new_mat

def determinant (A , total = 0) :
    # Section 1: store indices in list for row referencing
    indices = list(range(len(A)))
    
    # Section 2: when at 2x2 submatrices recursive calls end
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
 
    elif len(A) == 1:
        return A[0][0]
    # Section 3: define submatrix for focus column and 
    #      call this function
    for fc in indices: # A) for each focus column, ...
        # find the submatrix ...
        As = A[:] # B) make a copy, and ...
        As = As[1:] # ... C) remove the first row
        height = len(As) # D) 
        
        for i in range(height): 
            # E) for each remaining row of submatrix ...
            #     remove the focus column elements
            As[i] = As[i][0:fc] + As[i][fc+1:] 
 
        sign = (-1) ** (fc % 2) # F) 
        # G) pass submatrix recursively
        
        sub_det = determinant(As)
        # H) total all returns from recursion
        total += sign * A[0][fc] * sub_det 
 
    return total




def vertical_diagonal(matA):

    result = []
    mat_ = matA[:]
    for x in mat_:
        x.reverse()
        result.append(x)

    return result


def horizontal_diagonal(matA):

    result = []
    mat_ = matA[:]
    for x in range(len(matA) - 1, -1, -1):

        result.append(mat_[x])

    return result


def main_diagonal(matA):

    result = []
    for x in range(len(matA[0])):
        result.append([0] * len(matA))

    for x in range(len(matA[0])):
        for y in range(len(matA)):
            if x == y:
                result[x][y] = matA[x][y]
            else:
                result[x][y] = matA[y][x]

    return result


def side_diagonal(matB):

    result = []
    matB_ = matB[:]

    for x in matB_:        # 3 2 1
        x.reverse()        # 6 5 4
        result.append(x)   # 8 8 7

    # print(result)
    result1 = []
    for x in range(len(result[0])):
        result1.append([0] * len(result))

    # print(result1)
    main_result = []

    for x in range(len(result[0])):
        for y in range(len(result)):
            if x == y:
                result1[x][y] = result[x][y]

            else:
                result1[x][y] = result[y][x]

    for x in result1:
        x.reverse()
        main_result.append(x)

    return main_result

def matrix_input(a ,b):



    result = []

    for x in range(int(a)):
        mat_val = input().split()
        result.append(mat_val)



    main_result = result[:]

    for x in range(len(result)):
        for y in range(len(result[0])):
            if "."  in result[x][y]:
                main_result[x][y] = float(result[x][y])
            else:
                main_result[x][y] = int(result[x][y])


    return main_result


def mat_print(mat):

    for x in mat:
        for y in x:
            print(y, end=" ")

        print()


def mat_mul (matrix , factor):

    global order_A

    rows = order_A[0]
    columns = order_A[1]

    result = []
    for x in range(rows):
        result.append(["#"] * columns)

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            result[x][y] = matrix[x][y] * factor


    return result


def mat_sum(mat_A, mat_B):
    global order_A, order_B

    rows = order_A[0]
    columns = order_A[1]

    result = []
    for x in range(rows):
        result.append(["#"] * columns)

    for x in range(len(mat_A)):
        for y in range(len(mat_A[0])):
            result[x][y] = mat_A[x][y] + mat_B[x][y]

    return result


def matrix_multiplication (matA , matB):

    result = []

    for x in range(len(matA)):
        result.append([0] * len(matB[0]))


    for x in range(len(matA)):
        for y in range(len(matB[0])):
            for z in range(len(matA[0])):
                result[x][y] += (matA[x][z] * matB[z][y])

    return result


flag = True


while flag:

    print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
    num = int(input("Your choice: "))


    if num == 1:
        try:


            mat_A = []
            mat_B = []
            order_A = input("Enter size of first matrix: ").split(" ")
            order_A = [int(x) for x in order_A]
            print("Enter first matrix:")
            mat_A = matrix_input(order_A[0], order_A[1])


            order_B = input("Enter size of second matrix: ").split(" ")
            order_B = [int(x) for x in order_B]
            print("Enter second matrix:")
            mat_B = matrix_input(order_B[0], order_B[1])

            if order_A != order_B:
                print("ERROR")
                print()

            else:
                result = mat_sum(mat_A, mat_B)
                print("The result is:")
                mat_print(result)
                print()

        except Exception as e:
            print("The operation cannot be performed.\n")

    elif num == 2:

        try:

            mat_A = []
            mat_B = []
            order_A = input("Enter size of matrix: ").split(" ")
            order_A = [int(x) for x in order_A]
            print("Enter matrix:")
            mat_A = matrix_input(order_A[0], order_A[1])
            factor = input("Enter constant: ")

            if "." in factor:
                factor = float(factor)

            else:
                factor = int(factor)
            result = mat_mul(mat_A , factor)
            print("The result is:")
            mat_print(result)
            print()

        except Exception as e:
            print("The operation cannot be performed.\n")


    elif num == 3:
        try:


            mat_A = []
            mat_B = []
            order_A = input("Enter size of first matrix: ").split(" ")
            order_A = [int(x) for x in order_A]
            print("Enter first matrix:")
            mat_A = matrix_input(order_A[0], order_A[1])


            order_B = input("Enter size of second matrix: ").split(" ")
            order_B = [int(x) for x in order_B]
            print("Enter second matrix:")
            mat_B = matrix_input(order_B[0], order_B[1])

            if order_A[1]!= order_B[0]:
                print("The operation cannot be performed.\n")

            else:
                result = matrix_multiplication(mat_A, mat_B)
                print("The result is:")
                mat_print(result)
                print()

        except Exception as e:
            print(e)
            # print("The operation cannot be performed.\n")

    elif num == 4:
        print('''\n1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
        diag = int(input("Your choice: "))

        if diag == 1:
            order_A = input("Enter matrix size: ").split(" ")
            order_A = [int(x) for x in order_A]
            print("Enter matrix:")
            mat_A = matrix_input(order_A[0], order_A[1])
            result = main_diagonal(mat_A)
            print("The result is:")
            mat_print(result)
            print()

        elif diag == 2:
            order_A = input("Enter matrix size: ").split(" ")
            order_A = [int(x) for x in order_A]
            print("Enter matrix:")
            mat_A = matrix_input(order_A[0], order_A[1])
            result = side_diagonal(mat_A)
            print("The result is:")
            mat_print(result)
            print()

        elif diag == 3:
            order_A = input("Enter matrix size: ").split(" ")
            order_A = [int(x) for x in order_A]
            print("Enter matrix:")
            mat_A = matrix_input(order_A[0], order_A[1])
            result = vertical_diagonal(mat_A)
            print("The result is:")
            mat_print(result)
            print()

        elif diag == 4:
            order_A = input("Enter matrix size: ").split(" ")
            order_A = [int(x) for x in order_A]
            print("Enter matrix:")
            mat_A = matrix_input(order_A[0], order_A[1])
            result = horizontal_diagonal(mat_A)
            print("The result is:")
            mat_print(result)
            print()
    elif num == 0:
        flag = False
        exit()

    elif num == 5:
        order_A = input("Enter matrix size: ").split(" ")
        order_A = [int(x) for x in order_A]
        print("Enter matrix:")
        mat_A = matrix_input(order_A[0], order_A[1])
        result = determinant(mat_A)
        print("The result is:")
        print(result)
        print()

    elif num == 6:
        order_A = input("Enter matrix size: ").split(" ")
        order_A = [int(x) for x in order_A]
        print("Enter matrix:")
        mat_A = matrix_input(order_A[0], order_A[1])
        mat_det = determinant(mat_A)
        if order_A[0] <= 2 or order_A[1] <= 0:
            print("This matrix doesn't have an inverse.")

        elif mat_det == 0:
            print("This matrix doesn't have an inverse.\n")
        else:
            # mat_A = matrix_input(order_A[0], order_A[1])
            result = inverse(mat_A)
            # print(result)
            print("The result is:")
            mat_print(result)
            print()




# def vertical_diagonal(matA):

#     result = []
#     mat_ = matA[:]
#     for x in mat_:
#         x.reverse()
#         result.append(x)

#     return result


# def horizontal_diagonal(matA):

#     result = []
#     mat_ = matA[:]
#     for x in range(len(matA) - 1, -1, -1):

#         result.append(mat_[x])

#     return result


# def main_diagonal(matA):

#     result = []
#     for x in range(len(matA[0])):
#         result.append([0] * len(matA))

#     for x in range(len(matA[0])):
#         for y in range(len(matA)):
#             if x == y:
#                 result[x][y] = matA[x][y]
#             else:
#                 result[x][y] = matA[y][x]

#     return result


# def side_diagonal(matB):

#     result = []
#     matB_ = matB[:]

#     for x in matB_:        # 3 2 1
#         x.reverse()        # 6 5 4
#         result.append(x)   # 8 8 7

#     # print(result)
#     result1 = []
#     for x in range(len(result[0])):
#         result1.append([0] * len(result))

#     # print(result1)
#     main_result = []

#     for x in range(len(result[0])):
#         for y in range(len(result)):
#             if x == y:
#                 result1[x][y] = result[x][y]

#             else:
#                 result1[x][y] = result[y][x]

#     for x in result1:
#         x.reverse()
#         main_result.append(x)

#     return main_result
