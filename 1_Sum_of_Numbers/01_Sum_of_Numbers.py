#-----------------------------------------------------------------------------
# Name:        Sum of Numbers(01_Sum_of_Numbers.py)
# Purpose:     Create a program that asks the user for a number `n` and calculates the sum of all numbers from `1` to `n` using a `for` loop.
#
# Author:      LF
# Created:     12-March-2025
# Updated:     15-March-2025
#-----------------------------------------------------------------------------

print("Start")
#Get the number from the user
n = int(input("Enter a number: "))
#Start with a total of zero
total = 0
# Loop from 1 up to n (including n)
for i in range(1, n + 1):
#Add the current number to the total
    total += i
#Print the final sum
print("Sum = ", total)
print("Bye!")