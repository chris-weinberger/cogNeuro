import math
import itertools
import copy


# def generateVector(n):
#     vectors = []
#     for i in range(n):
#         vectors.append(0)
#     return vectors


# def generateVectors(n):
#     # matrix = []
#     # firstVec = generateVector(n)
#     # firstVec[0:32] = 1
#     # f_out = open("vectors.txt", "w")
    

#     #section generates the binary vectors with half on, half off

#     lst = list(map(list, itertools.product([0, 1], repeat=n)))

#     passable_vectors = []
#     for vector in lst:
#         num_ones = 0
#         for i in range(len(vector)):
#             if vector[i] == 1:
#                 num_ones += 1
#         if num_ones == n / 2:
#             passable_vectors.append(vector)
    
#     print('')
#     print('hello')
#     print(passable_vectors)




def printTheArray(arr, n):  
    for i in range(0, n):  
        print(arr[i], end = " ")  
      
    print()
    
def saveMatrix(matrix):
    f_out = open("vectors.csv", "w")

    for i in range(0, len(matrix)):
        string = ""
        for j in range(len(matrix[i])):
            if (j == len(matrix[0]) - 1):
                string += str(matrix[i][j])
            else:
                string += str(matrix[i][j]) + ", "
        string += "\n"
        f_out.write(string)
    f_out.close()

matrix = []
validFound = 0

def pearsonCorrelation(xVector, yVector):
    xAv = sum(xVector) / len(xVector)
    yAv = sum(yVector) / len(yVector)

    numerator = 0
    xDistance = 0
    yDistance = 0

    for index in range(len(xVector)):
        xDiff = xVector[index] - xAv
        yDiff = yVector[index] - yAv

        product = xDiff * yDiff
        numerator += product

        #denominator stuff
        xDistance += (xDiff * xDiff)
        yDistance += (yDiff * yDiff)
    
    denominator = math.sqrt(xDistance * yDistance)
    r = numerator / denominator
    return r

def testPearsonCorrelation(vector):
    #if matrix is empty, append first valid vector to it
    global validFound
    if len(matrix) == 0:
        matrix.append(vector)
        validFound += 1
        # return True #able to add vec
    else:
        valid = True
        #iterate through every vector in the matrix, and find r between the current vector and parameter vector
        for currVector in matrix:
            r = pearsonCorrelation(currVector, vector)
            if (r != 0):
                valid = False
                break 
        if valid:
            validFound += 1
            matrix.append(vector)
            # return True #able to add vec
        # else:
            # return False #able to add vec

# Function to generate all binary strings with given constraint:
# all vectors generated should be half-on, half-off
# inspired by code on geeksforgeeks by Rituraj Jain 
def generateAllBinaryStrings(n, arr, i):
    global validFound
    print(validFound)
    if validFound == n - 1:
        last_vec = []
        for i in range(n):
            last_vec.append(1)
        matrix.append(last_vec)
        saveMatrix(matrix)
        validFound += 1
        return
    if i == n: 
        # printTheArray(arr, n)
        testPearsonCorrelation(arr)
        return
      
    # First assign "1" at ith position  
    # only if abides by constraints
    # and try for all other permutations  
    # for remaining positions
    if(arr.count (1) < (n / 2)):
        arr[i] = 1
        generateAllBinaryStrings(n, copy.deepcopy(arr), i + 1)
        
    # And then assign "0" at ith position  
    # only if it abides by constraints
    # and try for all other permutations  
    # for remaining positions  
    if (arr.count(0) < (n / 2)):
        arr[i] = 0
        generateAllBinaryStrings(n, copy.deepcopy(arr), i + 1)  
    
  
# Driver Code  
if __name__ == "__main__":  
  
    n = 32
    arr = [None] * n  
  
    # Print all binary strings  
    generateAllBinaryStrings(n, arr, 0)

    #lastly, create the vector of all 1s, add to matrix
    last_vec = []
    for i in range(n):
        last_vec.append(1)
    matrix.append(last_vec)
    print(matrix)
    # saveMatrix(matrix)

# generateVectors(64)
