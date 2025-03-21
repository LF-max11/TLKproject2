#-----------------------------------------------------------------------------
# Name:        Countdown Timer(04_Countdown_Timer.py)
# Purpose:     Create a program that starts at `10` and counts down to `1`,
#              but if the user enters `"stop"`, the countdown should break.
# Author:      LF
# Created:     18-March-2025
# Updated:     19-March-2025
#-----------------------------------------------------------------------------

print("Start")
# Start the countdown from 10
count = 10

# Continue the countdown while count is greater than 0
while count > 0:
    # Print the current countdown number
    print(count)
    user_input = input('Enter "stop" to cancel or press Enter to continue: ')  # Ask user if they want to stop

    # If the user types "stop", exit the loop and stop the countdown
    if user_input.lower() == 'stop':
        # Inform the user that the countdown has been stopped
        print("Countdown stopped!")
        # Break out of the loop
        break

    # Decrease the countdown number by 1 if the user does not stop
    count -= 1

# End of countdown
