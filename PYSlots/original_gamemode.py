import random as rand
import sys, os

# This file will not be changed, due to it beong the original gamemode
def og_game():
    """
    og_game():
        - Description: 
            The original gamemode (the money gambled is **NOT** inputted) game function
        - Arguments:
            None
    """

    current_money = 1000 # Set the current amount of money to 1000 coins
    times_looped = 0 # Set the times the programme looped 0
    user_input_msg = "Press \"Y\" to continue, or press anything else to end:" # Set the message the user gets instructed to do at the end of each loop
    stopping_msg = "Stopping..." # Set the stopping message
    divider_msg = "==========" # Set the divider message
    slots_msg = "Slot Numbers" # Set the title message

    print(divider_msg) # Print the divider message before the loop to divide the game selected from the selection menu

    while (
        current_money > 0 # Loop while the user is not out of coins
    ):
        slot_one = rand.randint(1, 6) # Set the first slot to a random integer ranging from 1 to 6
        print(slot_one) # Print the first slot number

        slot_two = rand.randint(1, 6) # Set the second slot to a random integer ranging from 1 to 6
        print(slot_two) # Print the second slot number

        slot_three = rand.randint(1, 6) # Set the third slot to a random integer ranging from 1 to 6
        print(slot_three) # Print the third slot number

        print(divider_msg) # Print the divider message
        money_gambled = rand.randrange(100, 500, 1) # Set the amount of coins gambled to an integer ranging from 100 to 500 coins

        if (
            slot_one == slot_two == slot_three # Run if all slot numbers are the exact same
        ):
            current_money += round(money_gambled, None) # Add the coins gambled to the current coins the user has
            print("$" + str(current_money) + ".00") # Print the current coins from the previous line onto console
            print(divider_msg) # Print the divider message
        elif (
            slot_one == slot_two or slot_two == slot_three 
        ):
            current_money += round(money_gambled / 4, None)
            print("$" + str(current_money) + ".00")
            print(divider_msg) # Print the divider message
        elif (
            slot_one == slot_three
        ):
            current_money += round(money_gambled / 16, None)
            print("$" + str(current_money) + ".00")
            print(divider_msg) # Print the divider message
        elif (
            slot_one != slot_two != slot_three # Run if none of the slot numbers are the same
        ):
            current_money -= money_gambled # Subtract the current coin amount since the user lost this game
            if (
                current_money < 0 # Run if the user goes negative or hits exactly zero coins
            ):
                current_money = 0 # Set the user's coin amount to zero

                print("$" + str(current_money) + ".00") # Print "$0.00"

                print(divider_msg) # Print the divider message
                print(stopping_msg) # Print the stopping message
                print(divider_msg) # Print the divider message

                sys.exit(0) # rip
            elif (
                current_money == 0 # Run if the user is broke
            ):
                print("$" + str(current_money) + ".00")

                print(divider_msg) # Print the divider message
                print(stopping_msg) # Print the stopping message
                print(divider_msg) # Print the divider message

                sys.exit(0)
            else:
                print("$" + str(current_money) + ".00")
                print(divider_msg) # Print the divider message

        print(user_input_msg) # Print the instruction message
        print(divider_msg) # Print the divider message
        user_ans = input() # Have the user input "y" (or anything else)

        if (
            user_ans == "y"
            or user_ans == "Y"
            or user_ans == "yes"
            or user_ans == "Yes" # Run if the user confirms they want to play another round, otherwise exit the programme
        ):
            print(divider_msg) # Print the divider message
            print(slots_msg) # Print the title message
            print(divider_msg) # Print the divider message
        else:
            print(divider_msg) # Print the divider message
            print(stopping_msg) # Print the stopping message
            print(divider_msg) # Print the divider message
            sys.exit(0) # rip