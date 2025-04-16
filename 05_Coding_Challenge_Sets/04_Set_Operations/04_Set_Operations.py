# Name:         Set Operations(04_Set_Operations.py)
# Purpose:      To Combine and compare sets using set operations.
# Author:       LF
# Created:      07-April-2025
# Updated:      07-April-2025
#-----------------------------------------------------------------------------

print("Start")
#Print the sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
#Using union to combine both sets
print(set1.union(set2))
#Using intersection to see what is common between sets
print(set1.intersection(set2))
#Using difference to figure out what is different in between sets
print(set1.difference(set2))
print("End")