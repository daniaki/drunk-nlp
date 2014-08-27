''' Author  : Daniel Esposito
    Date    : 25/8/14
    Pupose  : Provides functions to conduct global and local edit distance 
              comparisons for sentence similarity measurement
'''
# Purpose: Takes two objects and compares them
# @param1,2: Objects to compare
# @return: 1 if different, 0 if the same
def deltaXY(x,y):
    if x == y: return 0
    else: return 2

# Purpose: Takes two strings and calculates the global edit distance
# @param1,2: Strings to compare
# @return: Integer representing edit distance
def globalEditDist(str1, str2):
    x = len(str1)
    y = len(str2)

    #Create editMatrix with 0's. Word to check against runs along j
    editMatrix = [[0 for i in range(0,y+1)] for j in range(0,x+1)]
    for i in range(0,x+1):
        editMatrix[i][0] = i
    for j in range(0, y+1):
        editMatrix[0][j] = j

    # Time for the good stuff
    for i in range(1,x+1):
        for j in range(1,y+1):
            if str1[i-1] == str2[j-1]:
                editMatrix[i][j] = editMatrix[i-1][j-1]
            else:
                editMatrix[i][j] = min(editMatrix[i][j-1], editMatrix[i-1][j],
                                       editMatrix[i-1][j-1])+1
    return editMatrix[x][y]

# Purpose: Determins if the edit distance neighbours around i and j are all zero
# @param1,2: index i and j > 0
# @param3: Matrix to check
# @return: True if all zero, false otherwise
def allZeros(i, j, matrix):
    x = matrix[i][j-1]
    y = matrix[i-1][j]
    z = matrix[i-1][j-1]
    if x+y+z > 0:
        return False
    else:
        return True

# Purpose: Takes a string str1 and looks for a substring match in str2
# @param1,2: Strings to compare
# @param3: defines the maximum difference from the maximum 
# @return: List of tuples with score and match position in str2
# TODO: implement back track and matches
def localAlignment(str1, str2, threshold):
    x = len(str1)
    y = len(str2)
    maxScore = 0
    matches = []

    #Create editMatrix with tuples. String to check against runs along j
    # tuple[0] is the score, tuple[1] is the back-pointer
    editMatrix = [[0 for i in range(0,y+1)] for j in range(0,x+1)]
    for i in range(0,x+1):
        editMatrix[i][0] = 0
    for j in range(0, y+1):
        editMatrix[0][j] = 0

    # Time for the good stuff
    for i in range(1,x+1):
        for j in range(1,y+1):
            if str1[i-1] == str2[j-1]:
                editMatrix[i][j] = max(editMatrix[i][j-1], editMatrix[i-1][j],
                                       editMatrix[i-1][j-1])+1
            else:
                if allZeros(i, j, editMatrix):
                    editMatrix[i][j] = 0
                else: 
                    editMatrix[i][j] = max(editMatrix[i][j-1], editMatrix[i-1][j],
                                       editMatrix[i-1][j-1])-1
    #Find the maximum score
    for i in range(0,x+1):
        maxScore = max(maxScore, max(editMatrix[i]))
    if maxScore + threshold < len(str1):
        return []
    else:
        return maxScore

# Purpose: Debug only
def printMatrix(m,x,y):
    for i in range(0,x+1):
        line = ""
        for j in range(0,y+1):
            line += ' ' + str(m[i][j])
        print(line)
        print('\n')
