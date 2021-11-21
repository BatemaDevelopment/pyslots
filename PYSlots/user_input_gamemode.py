import random as rand
import sys, os

def user_input_game():
    """
    user_input_game():
        - Description: 
            The user input (the money gambled is inputted) game function
        - Arguments:
            None
    """

    current_money = 1000
    user_input_msg = "Press \"Y\" to continue, or press anything else to end:"
    user_money_input_msg = "Type the money amount you want to gamble (100-1000):"
    stopping_msg = "Stopping..."
    divider_msg = "=========="
    slots_msg = "Slot Numbers"

    print(divider_msg)

    while current_money > 0:
        print(user_money_input_msg)
        print(divider_msg)

        money_gambled = input()
        
        print(divider_msg)

        try:
            if (
                int(money_gambled) > current_money
            ):
                print("You do not have enough money to gamble that amount! Please try again!")
                print(divider_msg)
            elif (
                int(money_gambled) < 100 
                and current_money >= 100
            ):
                print("Please gamble an amount that is 100+.")
                print(divider_msg)
            elif (
                int(money_gambled) >= 100 
                and current_money > 100
            ):
                print(slots_msg)
                print(divider_msg)

                slot_one = rand.randint(1, 6)
                print(slot_one)

                slot_two = rand.randint(1, 6)
                print(slot_two)

                slot_three = rand.randint(1, 6)
                print(slot_three)

                if (
                    slot_one == slot_two == slot_three
                ):
                    current_money += round(int(money_gambled), None)
                    print("$" + str(current_money) + ".00")
                    print(divider_msg)
                elif (
                    slot_one == slot_two or slot_two == slot_three
                ):
                    current_money += round(int(money_gambled) / 4, None)
                    print("$" + str(current_money) + ".00")
                    print(divider_msg)
                elif (
                    slot_one == slot_three
                ):
                    current_money += round(int(money_gambled) / 16, None)
                    print("$" + str(current_money) + ".00")
                    print(divider_msg)
                elif (
                    slot_one != slot_two != slot_three
                ):
                    current_money -= int(money_gambled)
                    if current_money < 0:
                        current_money = 0

                        print("$" + str(current_money) + ".00")

                        print(divider_msg)
                        print(stopping_msg)
                        print(divider_msg)

                        sys.exit(0)
                    elif current_money == 0:
                        print("$" + str(current_money) + ".00")

                        print(divider_msg)
                        print(stopping_msg)
                        print(divider_msg)

                        sys.exit(0)
                    else:
                        print(divider_msg)
                        print("$" + str(current_money) + ".00")
                        print(divider_msg)

                print(user_input_msg)
                print(divider_msg)

                user_ans = input()

                if (
                    user_ans == "y" 
                    or user_ans == "Y" 
                    or user_ans == "yes" 
                    or user_ans == "Yes"
                ):
                    print(divider_msg)
                else:
                    print(stopping_msg)
                    print(divider_msg)
                    sys.exit(0)
        except ValueError:
            print("Please type only a number between 100 and 1000 to proceed. Please try again!")
            print(divider_msg)