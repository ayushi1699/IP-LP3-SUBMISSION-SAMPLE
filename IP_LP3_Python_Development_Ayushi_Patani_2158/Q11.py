# CODING QUESTIONS:11 Write a Python program to get a week number.
# Sample Date :
#  2015, 6, 16
# Expected Output :
# 25

import datetime
y, m, d = input("Enter date:(yyyy,mm,dd) ").split(",")
y = int(y)
m = int(m)
d = int(d)
week_no = datetime.date(y, m, d).isocalendar()[1]
print(week_no)

# output:
# Enter date:(yyyy,mm,dd) 2015, 6, 16
# 25
