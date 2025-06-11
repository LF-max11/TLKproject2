# start
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# ask the user to enter a number
num = int(input("Enter a number: "))

# check and print only one result
print(is_even(num))
