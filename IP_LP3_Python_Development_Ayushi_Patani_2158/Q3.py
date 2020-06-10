# CODING QUESTIONS:3 You are given n-words. Some words may repeat. For each word, output its number of occurrences.
# The output order should correspond with the input order of the appearance of the word. See the sample input/output
# for clarification.
# Constraints
# 1<_n<_10​5
# The sum of the lengths of all the words do not exceed ​ 10​6
# All the words are composed of lowercase English letters only.
# Input Format
# The first line contains the integer,n.
# The next n lines each contain a word.
# Output Format
# Output 2  lines.
# On the first line, output the number of distinct words from the input.
# On the second line,output the number of occurrences for each distinct word according to their appearance in the input.
# Sample Input
# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Sample Output
# 3
# 2 1 1
n = int(input())
if(n <1 or n > 100000):
    print("n is out of range(1,100000)")
    exit(0)
words = []
freq = []
length = 0
for i in range(0, n):
    inp = input()
    if(inp.isalpha() == False or inp.islower() == False):
        print("String should have only lower case english alphabets.")
        exit(0)
    length += len(inp)
    if(i == 0):
        words.append(inp)
        freq.append(1)
    else:
        x = 0
        count = 0
        for val in words:
            if(inp == val):
                x = 1
                break
            count += 1
        if(x == 0):
            words.append(inp)
            freq.append(1)
        else:
            freq[count] += 1

if(length > 160):
    print("The total length of all words exceeded 160")
    exit(0)

print(len(words))
for i in freq:
    print(i, end=" ")

#output
#IP:
#4
# bcdef
# abcdefg
# bcde
# bcdef
#OP:
#3
#2 1 1
