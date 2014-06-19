#
# Given a triangle of numbers, finds the maximum sum possible
# along a path from the top of the triangle to the bottom
#

#
# Triangles are represented as a 2D array; see the test routines
# in main() for examples
#

#
# TODO: add a routine to read input from stdin or a text file
#       track values to reach solution from top to bottom
#

__author__ = "bsloan"

def max_sum(T):
    # given a triangle T represented as a two-dimensional array
    # returns the maximum sum from top to bottom

    row = len(T) - 2        # start at second-to-bottom row
    row_length = len(T[0])  # all rows have equal number of columns
    sum = 0

    while row >= 0:                      # loop from bottom up (stop at the top of triangle)
        for i in range(row_length):      # for each value in this row left to right...
            if T[row][i] == -1: continue # end of row reached; skip to next
            sum = T[row][i]

            # get the two candidate solutions from the row below
            opt1 = T[row + 1][i]         # (best answer built from left-hand sub-triangle)
            opt2 = T[row + 1][i + 1]     # (best answer built from right-hand sub-triangle)

            # best solution possible at this position will be larger of opt1 and opt2
            sum += max(opt1, opt2)

            # store the sum at this position to use when processing the next row up
            T[row][i] = sum
        row -= 1                         # do the next row up
    return sum

def main():
    # test routines for max_sum
    A = [[4,-1,-1,-1],
         [7, 4,-1,-1],
         [2, 4, 6,-1],
         [8, 5, 9, 3]]

    # solution to triangle A is 24
    sol_A = max_sum(A)
    if sol_A == 24: print "Solution to A is correct: 24"
    else:
        print "incorrect"

    B = [[53,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],
        [200, 159,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],
        [182,  28, 190,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],
        [197, 103, 143, 123,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],
        [ 35,  73,  39,  89, 105,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],
        [193,  42, 168,   1,  49,  23,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],
        [110,  87,  31,  99,  40, 199, 159,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],
        [ 65, 117, 155, 128,  76,  99, 102,  81,  -1,  -1,  -1,  -1,  -1,  -1,  -1],
        [ 44,   4, 171, 110,  64, 142, 164,  93, 142,  -1,  -1,  -1,  -1,  -1,  -1],
        [ 73,  51,   1, 133,  41,  68,  88,  58,  98, 118,  -1,  -1,  -1,  -1,  -1],
        [113, 196,  44,  24, 199, 164,  41, 108, 134,  21,   4,  -1,  -1,  -1,  -1],
        [ 42, 140,  37,  55, 168,  40,  81, 115, 134, 184, 119,  91,  -1,  -1,  -1],
        [ 66, 118,  59,  24, 149,   9,  29, 105,  34,  62, 154,  42, 167,  -1,  -1],
        [ 82,  88, 120, 105, 167, 113, 107,  59,  72,  35, 147, 164, 139,  70,  -1],
        [147, 158,  76,  57, 131,  48,  56, 119, 156,  86, 159,  36, 108, 120, 118]]

    # solution to triangle B is 2220
    sol_B = max_sum(B)
    if sol_B == 2220: print "Solution to B is correct: 2220"
    else:
        print "Solution to B is incorrect"

if __name__ == "__main__":
    main()
