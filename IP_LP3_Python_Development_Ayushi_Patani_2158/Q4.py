# CODING QUESTIONS:4 Little Robert likes mathematics. Today his teacher has given him two integers and
# asked to find out how many integers can divide both the numbers.
# Would you like to help him in completing his school assignment?
# Input Format :
# There are two integers, a and b as input to the program.
# Output Format:
# Print the number of common factors of a and b. Both the input value should be in a range of 1 to 10^12.
# Input:  10  15
# Output:
#  2

a, b = input().split(" ")
a = int(a)
b = int(b)
if(a < 1 or a > 1000000000000 or b < 1 or b > 1000000000000):
    print("Numbers should be in the range (1,1000000000000)")
    exit(0)
n = 0
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        n += 1
print(n)

#output:
#IP: 10 15
#OP: 2