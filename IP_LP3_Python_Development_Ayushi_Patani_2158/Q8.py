# CODING QUESTIONS:8 Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)...
# (until n-x =< 0).
# Test Data:
# sum_series(6) -> 12
# sum_series(10) -> 30
x = int(input("Enter a positive no: "))
num = x
if(x < 0):
    print("Negative values not allowed")
    exit(0)
sum = 0
while(x >= 0):
    sum += x
    x -= 2
print("sum_series("+str(num)+") -> "+str(sum))

#output:
# Enter a positive no: 10
# sum_series(10) -> 30
