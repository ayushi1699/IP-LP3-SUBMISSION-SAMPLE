#CODING QUESTIONS:10
# Write a Python program to sort a list of elements using the selection sort algorithm.
# Note: The selection sort improves on the bubble sort by making only one exchange for every pass through the list.
# Sample Data:
# [14,46,43,27,57,41,45,21,70]
# Expected Result:
# [14, 21, 27, 41, 43, 45, 46, 57, 70]

lst = []
n = int(input("Enter number of elements in the array: "))
for i in range(n):
    x = int(input("Enter element "+str(i+1)+": "))
    lst.append(x)
print(lst)
for i in range(0,n):
    for j in range(i+1,n):
        if(lst[i] > lst[j]):
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

print(lst)

# output:
# Enter number of elements in the array: 9
# Enter element 1: 14
# Enter element 2: 46
# Enter element 3: 43
# Enter element 4: 27
# Enter element 5: 57
# Enter element 6: 41
# Enter element 7: 45
# Enter element 8: 21
# Enter element 9: 70
# [14, 46, 43, 27, 57, 41, 45, 21, 70]
# [14, 21, 27, 41, 43, 45, 46, 57, 70]