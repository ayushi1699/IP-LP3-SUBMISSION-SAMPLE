# CODING QUESTIONS:5
# You have given a string. You need to remove all the duplicates from the string.
# The final output string should contain each character only once. The respective order of the characters inside the
# string should remain the same. You can only traverse the string at once.
# Input string:
# ababacd
# Output string:
# abcd

inp_str = input()
n = len(inp_str)
for i in range(0,n):
    count = 0
    for j in range(0,i):
        if(inp_str[i] == inp_str[j]):
            count = 1
            break
    if(count == 0):
        print(inp_str[i], end="")


#output:
#IP:ababacd
#OP:abcd