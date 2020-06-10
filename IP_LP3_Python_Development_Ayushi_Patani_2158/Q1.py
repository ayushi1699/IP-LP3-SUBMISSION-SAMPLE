# Coding Question1
# Read two integers from STDIN and print three lines where:
# ● The first line contains the sum of the two numbers.
# ● The second line contains the difference between the two numbers (first - second).
# ● The third line contains the product of the two numbers.
# Input Format
# The first line contains the first integer, a.
# The second line contains the second integer, b.
# Constraints
# 1<_a<_10​10
# 1<_b<_10​10
# Output Format
# Print the three lines as explained above.
# Sample Input
# 3    2
# Sample Output
# 5  1   6
a, b = input().split(" ")
a = int(a)
b = int(b)
if(a < 1 or a> 10000000000 or b < 1 or b > 100000000000):
    print("Data out of Range (Numbers should be in range (1,10^10))")
else:
    c = a+b
    print(c, end=" ")
    d = a-b
    print(d, end=" ")
    e = a*b
    print(e, end=" ")
#output
#IP: 3 2
#OP: 5 1 6
