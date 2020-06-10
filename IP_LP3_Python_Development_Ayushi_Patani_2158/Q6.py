# CODING QUESTIONS:6
# Given a matrix of size m*n, m denotes the row starting with index 0 and n denotes the column starting with index 0.
# The matrix will hold distinct integers as elements.
# We need to find a distinct number of positional elements which are either the minimum or maximum in their
# corresponding row or column.
# Please return -1 if any row or any column has multiple minimum or maximum              elements.
# For example, given a matrix of size 3*3, the elements are stored as follows.
# 1  3  4
# 5  2  9
# 8  7  6
# The expected output is 7.
# In the above example, we identified the output as 7 based on below.
# 1 - minimum in row and column
# 4 - Maximum in row
# 2 - Minimum in column and row
# 9 - Maximum in row and column
# 8 - Maximum in row and column
# 7 - Maximum in column
# 6 - Minimum in row
# Input: m - integer - number of rows n - integer - number of columns
# m * n matrix
# Output:
# r - integer - result
# Constraints: 0<m,n<100
# Elements in the matrix are positive integers.

M = int(input("Enter no of rows : "))
N = int(input("Enter no of columns : "))
Mat = []
for i in range(0, M):
    col = []
    for j in range(0, N):
        x = int(input("Enter element ["+ str(i)+"]["+str(j)+"]: "))
        col.append(x)
    Mat.append(col)
min_max = []
check = 0
num = 0
for i in range(0, M):
    check = 0
    x = min(Mat[i])
    y = max(Mat[i])
    c_x = Mat[i].count(x)
    c_y = Mat[i].count(y)
    if(c_x >1 or c_y >1):
        check = 1
        break;
    if(check == 1):
        num = -1
        break
    else:
        try:
            ch = min_max.index(x)
        except ValueError:
            min_max.append(x)
        try:
            ch = min_max.index(y)
        except ValueError:
            min_max.append(y)

if(num == -1):
    print(-1)
else:
    num = 0
    for i in range(0,N):
        c = []
        for j in range(0,M):
            c.append(Mat[j][i])
        check = 0
        x = min(c)
        y = max(c)
        c_x = c.count(x)
        c_y = c.count(y)
        if (c_x > 1 or c_y > 1):
            check = 1
            break
        if (check == 1):
            num = -1
            break
        else:
            try:
                ch = min_max.index(x)
            except ValueError:
                min_max.append(x)
            try:
                ch = min_max.index(y)
            except ValueError:
                min_max.append(y)
    if(num == -1):
        print(-1)
    else:
        print(len(min_max))

#output:
#IP:
# 1  3  4
# 5  2  9
# 8  7  6
#OP: 7