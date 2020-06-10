# CODING QUESTIONS:9 Write a Python program to check whether a given a binary tree is a valid binary search tree (BST)
# or not.Let a binary search tree (BST) is defined as follows: The left subtree of a node contains only nodes with keys
# less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#    1   3
#    Binary tree [2,1,3], return true.
#
# Example 2:
# 1
# / \
# 2   3
# Binary tree [1,2,3], return false.
h = int(input("Enter Height of Binary tree"))
n = (2 ** h) - 1
BST = []
for i in range(n):
    x = int(input("Enter node: "))
    BST.append(x)
check = (2 ** (h-1)) -1
for i in range(check):
    if(BST[i] < BST[2*i +1] or BST[i] > BST[2*i+2]):
        print("False")
        exit(0)

print("True")

#output
#Enter Height of Binary tree2
# Enter node: 2
# Enter node: 1
# Enter node: 3
# True
