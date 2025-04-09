# Name:         Adding and Removing Elements(06_Adding_and_Removing_Elements.py)
# Purpose:      To Modify a set efficiently.
# Author:       LF
# Created:      08-April-2025
# Updated:      08-April-2025
#-----------------------------------------------------------------------------


print("Start")
#Create a set and name it letters
letters = {'a', 'b', 'c'}
# Add multiple elements by using .update()
letters.update({'d', 'e', 'f'})
#Remove 'b' using .discard()
letters.discard('b')
#Print the letters to get updated list
print(letters)
print("End")