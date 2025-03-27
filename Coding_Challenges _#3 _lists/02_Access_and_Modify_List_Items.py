#-----------------------------------------------------------------------------
# Name:       Access and Modify List(02_Access_and_Modify_List_Items.py)
# Purpose:    To Modify a grocery list by changing an existing item.
#
# Author:      LF
# Created:     27-March-2025
# Updated:     27-March-2025
#-----------------------------------------------------------------------------

print("Start")
print("Here's a grocery list")

#Writing a grocery list
grocery_list = ['Apple', 'Banana', 'Carrots', 'Milk', 'Bread']
# Changing the second item in the list (index 1) from 'Banana' to 'Grapes'
grocery_list[1] = 'Grapes'
#printing the updated grocery list
print(grocery_list)
#printing the third item from the list
print(grocery_list[2])

print("End")